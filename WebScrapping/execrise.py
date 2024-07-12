    # execrise1 : scrape data from the http://openweathermap.org
# current weatherdata
import requests
import csv
import json

# Step 1: Get your API key from OpenWeatherMap
api_key = '336e6e8bd4820f250616b1c3d5529e08'
city = 'Kampala'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# Step 2: Fetch the weather data
response = requests.get(url)
weather_data = response.json()

# Step 3: Parse the JSON response to extract required data
city_name = weather_data['name']
temperature = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
description = weather_data['weather'][0]['description']

# Step 4: Save the data to a CSV file
csv_file = 'weather_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["City", "Temperature (C)", "Humidity (%)", "Wind Speed (m/s)", "Description"])
    writer.writerow([city_name, temperature, humidity, wind_speed, description])

# Step 5: Save the data to a JSON file
data = {
    'name': city_name,
    'temperature': temperature,
    'humidity': humidity,
    'wind_speed': wind_speed,
    'description': description
}
json_file = 'weather_data.json'
with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Step 6: Print a success message
print(f'Data saved successfully to {csv_file} and {json_file} format')
