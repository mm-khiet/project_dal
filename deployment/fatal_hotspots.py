from flask import Flask, render_template_string, jsonify
import csv

app = Flask(__name__)

# Function to read data from CSV file
def read_csv_data(filepath):
    with open(filepath, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [
            {
                "latitude": float(row["LATITUDE"]),
                "longitude": float(row["LONGITUDE"]),
                "deaths": int(row["deaths"])  # Assuming the column for deaths is lowercase. Adjust if needed.
            } for row in csv_reader
        ]
    return data

# Replace 'grouped_points_summary2.csv' with your actual CSV file path if it's located in a different directory
DATA = read_csv_data('../grouped_points_summary2.csv')

@app.route("/")
def index():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Death Locations Map</title>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC084aX_CBC9WloaPJQxxlMZ2GxXB3loh8"></script>
    <script>
        async function initMap() {
            const map = new google.maps.Map(document.getElementById('map'), {
                zoom: 10,
                center: {lat: (41.640 + 42.023) / 2, lng: (-87.940 + -87.524) / 2},
            });

            // Fetch the data from the server
            const response = await fetch('/data');
            const locations = await response.json();

            // Add a marker for each location
            locations.forEach(location => {
                const markerSize = Math.max(location.deaths, 1); // Ensure size is at least 1
                new google.maps.Marker({
                    position: {lat: location.latitude, lng: location.longitude},
                    map: map,
                    // Use a scaled size to make the marker larger for more deaths
                    icon: {
                        path: google.maps.SymbolPath.CIRCLE,
                        scale: markerSize, // Adjust this scaling factor as needed
                        fillColor: 'red',
                        fillOpacity: 0.5,
                        strokeWeight: 0.4
                    },
                });
            });
        }
    </script>
</head>
<body onload="initMap()">
    <div id="map" style="height: 1000px; width: 100%;"></div>
</body>
</html>
    """)

@app.route("/data")
def data():
    return jsonify(DATA)

if __name__ == "__main__":
    app.run(debug=True)

# <div id="map" style="height: 500px; width: 100%;"></div>
