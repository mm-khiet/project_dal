# Exploring and Predicting Traffic Accident Injury Severity in Urban Areas

## Introduction
This is a python implementation for predicting car crashes injury severity in Chicago city.<br>

## Requirements
1. Python3.11<br>
2. Install the packages from the requirments files.<br>
~~~python
pip install -r requirements.txt
~~~

## Record of the data acquisition process
The data acquired from: https://catalog.data.gov/dataset/traffic-crashes-crashes<br>
The above website belongs to USA government free datasets advised by the course instructions.<br>
No need to download it manually, the Python code will handle this the first time it runs.<br>

<br>

## Running the hotspots tool
1. Clone the project.
2. Navigate to deployment directory:
~~~
cd deployment
~~~
3. Run the desired hotspot emulator:
~~~
# For Fatals hotspots and it density
python fatal_hotspots.py

# For Heavy Injuries hotspots and it density
python injured_hotspots.py

~~~
4. Now a web server should be up with the required information that acquired from prepared datasets (you may use them or customize them via our code) - In the browser open the following URL:
~~~
http://127.0.0.1:5000
~~~

