import time
from dotenv import load_dotenv

# Import custom modules
from Engine.speech import listen
from Engine.tts import speak
from Engine.brain import get_ai_response

from core.intent_classifier import IntentClassifier
from core.command_router import CommandRouter
from core.memory import Memory
memory = Memory()

classifier = IntentClassifier()
router = CommandRouter()

load_dotenv()
# Add state variable
pending_weather = False

def process_command(command):

    if not command or not isinstance(command, str):
        return None

    command = command.lower().strip()

    if command == "jarvis":
        return None

    if any(word in command for word in ["stop", "exit", "shutdown","shut down", "quit"]):
        return "Shutting down. Goodbye."

    intent = classifier.classify(command)

    response = router.route(intent, command)

    if response:
        return response

    return get_ai_response(command)

def main():
    speak("Jarvis is online. Say Jarvis to wake me up.")

    while True:
        text = listen(timeout=5)
        if not text:
            continue

        if "jarvis" in text:
            name = memory.get("user_name")

            if name:
                speak(f"I am listening, {name}.")
            else:
                speak("I am listening.")

            while True:
                command = listen(timeout=5)
                if not command:
                    continue

                if any(word in command for word in ["sleep", "quit"]):
                    speak("Going to sleep.")
                    break

                if "shutdown" in command:
                    speak("Shutting down. Goodbye.")
                    exit(0)

                response = process_command(command)
                if response:
                    speak(response)

                time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("Shutting down. Goodbye.")
        exit(0)
