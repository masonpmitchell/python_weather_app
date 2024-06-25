import requests

city = input("Enter your city: ")

api_key = "3ccf6bee1a76de97cd4fcac908586671"
response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}")

if response.status_code == 200:
    # Accessing the first element in the 'list' which contains the forecast details
    forecast_data = response.json()['list'][0]
    weather_description = forecast_data['weather'][0]['main']
    temperature = forecast_data['main']['temp'] - 273
    
    print(f"Weather: {weather_description}, Temperature: {temperature}C")
else:
    print("Failed to get the weather data. Please check the city name and try again.")