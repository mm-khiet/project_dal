import requests
import os
import pandas as pd

G_UTILITIES_DIRECTOR = "dataset"
G_UTILITIES_FILENAME = "chicago_data.csv"


def download_dataset():
    # URL of the CSV file
    url = "https://data.cityofchicago.org/api/views/85ca-t3if/rows.csv?accessType=DOWNLOAD"

    # Full path to the file
    file_path = os.path.join(G_UTILITIES_DIRECTOR, G_UTILITIES_FILENAME)

    # Create the directory if it does not exist
    if not os.path.exists(G_UTILITIES_DIRECTOR):
        os.makedirs(G_UTILITIES_DIRECTOR)

    # Check if the file already exists
    if not os.path.isfile(file_path):
        print(f"Downloading the {G_UTILITIES_FILENAME}...")
        response = requests.get(url)
        # Ensure the request was successful
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
        else:
            print("Failed to download the file. Status code:", response.status_code)
            return False
    else:
        print("File already exists...")
    return True


def read_data():
    return pd.read_csv(f"{G_UTILITIES_DIRECTOR}/{G_UTILITIES_FILENAME}")


def acquire_dataset():
    download_dataset()
    return read_data()
