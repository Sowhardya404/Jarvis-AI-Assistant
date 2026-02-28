class IntentClassifier:

    def classify(self, text: str) -> str:
        text = text.lower()

        if "weather" in text:
            return "weather"

        elif any(word in text for word in ["time", "date"]):
            return "datetime"

        elif "play" in text:
            return "music"

        elif any(word in text for word in ["volume", "brightness", "open"]):
            return "system"

        elif "my name is" in text:
            return "set_name"

        elif "reset memory" in text:
            return "reset_memory"

        else:
            return "ai_fallback"