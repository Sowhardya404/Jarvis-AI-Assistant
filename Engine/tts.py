import pyttsx4
import re

# 1. Initialize the engine once
# 'sapi5' is the Microsoft speech API for Windows voices
engine = pyttsx4.init('sapi5') 

# 2. Set Properties (Optional but recommended)
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)  # Standard is 200; 170 sounds more natural
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0) # 0.0 to 1.0

def clean_llm_output(text):
    """Removes markdown symbols like ** or __ so Jarvis doesn't say them."""
    text = re.sub(r'(\*\*|\*|__|_)', '', text)
    text = text.replace('`', '')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def speak(text):
    """The main function you will import into main.py"""
    cleaned_text = clean_llm_output(text)
    print(f"Jarvis: {cleaned_text}")
    
    # say() queues the command, runAndWait() actually plays it
    engine.say(cleaned_text)
    engine.runAndWait()