import Tools.jarvis_controls as controls


class SystemCommand:

    def execute(self, text):

        text = text.lower()

        if "volume up" in text:
            controls.increase_volume()
            return "Volume increased."

        elif "volume down" in text:
            controls.decrease_volume()
            return "Volume decreased."

        elif "brightness up" in text:
            controls.increase_brightness()
            return "Brightness increased."

        elif "brightness down" in text:
            controls.decrease_brightness()
            return "Brightness decreased."

        elif "open" in text:
            target = text.replace("open", "").strip()
            response = controls.open_application(target)

            if not response:
                response = controls.open_website(target)

            return response

        return None