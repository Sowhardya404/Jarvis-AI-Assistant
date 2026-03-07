import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "models/gemini-2.5-flash"

conversation_history = []

def get_ai_response(prompt):
    global conversation_history

    conversation_history.append(f"User: {prompt}")

    try:
        full_prompt = (
            "You are Jarvis, a smart, concise AI assistant.\n\n"
            + "\n".join(conversation_history)
            + "\nJarvis:"
        )

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=full_prompt
        )

        raw_text = response.text
        reply = raw_text.strip() if isinstance(raw_text, str) else "I couldn't generate a response."
        conversation_history.append(f"Jarvis: {reply}")

        return reply

    except Exception as e:
        print("Gemini Error:", e)
        return "AI service is currently unavailable."
