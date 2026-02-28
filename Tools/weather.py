import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    if not OPENWEATHER_API_KEY:
        return "Weather API key is missing."

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"The current temperature in {city} is {temp}°C with {desc}."
        else:
            return "Sorry, I couldn't find that city."

    except Exception as e:
        print(f"Weather Error: {e}")
        return "Unable to fetch weather right now."
