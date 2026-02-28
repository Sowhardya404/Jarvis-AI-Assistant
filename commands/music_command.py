from Tools.musiclibrary import play_song
from core.memory import Memory


class MusicCommand:

    def __init__(self):
        self.memory = Memory()

    def execute(self, text):

        text = text.lower().strip()
        song = text.replace("play", "").strip()

        if song:
            self.memory.save("last_song", song)
            return play_song(song)

        saved_song = self.memory.get("last_song")

        if saved_song:
            return play_song(saved_song)

        return "What song would you like to play?"