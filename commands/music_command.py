from Tools.musiclibrary import play_song
from core.memory import Memory


class MusicCommand:

    def __init__(self):
        self.memory = Memory()

    def execute(self, text):

        text = text.lower().strip()

        # If user asks for previous song
        if "last song" in text or "previous song" in text:
            saved_song = self.memory.get("last_song")

            if saved_song:
                return play_song(saved_song)
            else:
                return "No previous song found."
        
        # Normal play Command
        song = text.replace("play", "").strip()

        if song:
            self.memory.save("last_song", song)
            return play_song(song)

        saved_song = self.memory.get("last_song")

        if saved_song:
            return play_song(saved_song)

        return "What song would you like to play?"