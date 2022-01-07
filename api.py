# import module sys to get the type of exception
import sys

# needed to make web requests
import requests

# convert the response as a strcuctured json
import json

# input
geo_values = input(
    "\nEnter the latitude longitude value sepearted by single comma : ")

# making url
url = "https://api.weather.gov/points/"+geo_values


# getting data
try:

    # requesting url
    res = requests.get(url)

    # make json object
    data = json.loads(res.text)
    properties = data['properties']

    # getting forecast url
    forecast = properties['forecast']

    # getting forecast data
    forecast_res = requests.get(forecast)
    forecast_data = json.loads(forecast_res.text)
    forecast_properties = forecast_data['properties']
    forecast_periods = forecast_properties['periods']

    # finding wednesday night temperature
    for period in forecast_periods:
        if period['number'] == 13:
            print(period['temperature'])
            break

except:
    print("Oops!", sys.exc_info()[0], "occurred.")
