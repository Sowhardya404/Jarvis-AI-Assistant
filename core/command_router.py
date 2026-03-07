from commands.weather_command import WeatherCommand
from commands.music_command import MusicCommand
from commands.datetime_command import DateTimeCommand
from commands.system_command import SystemCommand
from commands.news_command import NewsCommand
from core.memory import Memory

class CommandRouter:

    def __init__(self):
        self.commands = {
            "weather": WeatherCommand(),
            "music": MusicCommand(),
            "datetime": DateTimeCommand(),
            "system": SystemCommand(),
            "news": NewsCommand()
        }
        self.memory = Memory()

    def route(self, intent, text):

        if intent == "set_name":
            name = text.replace("my name is", "").strip()
            self.memory.save("user_name", name)
            return f"Nice to meet you, {name}."

        if intent == "reset_memory":
            self.memory.save("default_city", None)
            self.memory.save("last_song", None)
            self.memory.save("user_name", None)
            return "Memory has been reset."

        command = self.commands.get(intent)

        if command:
            return command.execute(text)

        return None