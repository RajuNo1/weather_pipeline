import requests
import datetime

def fetch_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return {
        "city": city,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "temp_c": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "weather": data['weather'][0]['description']
    }
