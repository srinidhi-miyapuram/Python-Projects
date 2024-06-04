import requests

name = input("Enter the city name :- ")
api_key = "<Enter your api key here>"

params = {"q": name, "appid": api_key, "units": "metric"}

# For temperature in Fahrenheit and wind speed in miles/hour, use units=imperial
# For temperature in Celsius and wind speed in meter/sec, use units=metric
# Temperature in Kelvin and wind speed in meter/sec is used by default, so there
# is no need to use the units parameter in the API call if you want this

url = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(url, params).json()

print(f"Current temperature in {name} is {response["main"]["temp"]}{chr(176)} C")