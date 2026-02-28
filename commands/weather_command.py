from Tools.weather import get_weather
from core.memory import Memory


class WeatherCommand:

    def __init__(self):
        self.memory = Memory()

    def execute(self, text):

        text = text.lower().strip()

        # If user only says "weather"
        if text == "weather":
            saved_city = self.memory.get("default_city")

            if saved_city:
                return get_weather(saved_city)

            return "Which city should I check?"

        # Otherwise extract city
        words = text.split()
        city = words[-1]

        self.memory.save("default_city", city)

        return get_weather(city)