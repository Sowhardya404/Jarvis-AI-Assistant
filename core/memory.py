import json
import os


class Memory:
    def __init__(self, filename="memory.json"):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f)

    def _read(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def _write(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def save(self, key, value):
        data = self._read()
        data[key] = value
        self._write(data)

    def get(self, key):
        data = self._read()
        return data.get(key)