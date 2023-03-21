# Get API Key : https://openweathermap.org/api
import requests
import json

api_key = "8bdc67502b740ebdd020cbbde6f76225"
city = 'London'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_key)
response = requests.get(url)
data = response.json()

print(data)
weather = (data['weather'][0]['description'])
print("Today, we have " + weather)

t = data['main']['temp']
c = t - 273.15
print("Temperature is " + str(c) + "C")

pressure = (data['main']['pressure'])
print("The pressure is at " + str(pressure))

humidity = (data['main']['humidity'])
print("Today's humidity is " + str(humidity))

sunset = (data['sys']['sunset'])
print("The time for today's sunset is at " + "sunset" + ".")

# Temp, Weather, Humidity, Pick one thing he didn't give the code for and display
