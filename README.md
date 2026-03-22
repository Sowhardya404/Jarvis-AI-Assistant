# Jarvis AI Assistant 🤖

A voice-activated AI assistant built with Python, powered by Google Gemini.
Responds to voice commands for weather, music, news, system controls, and general conversation.

---

## Features

- Voice activation — say "Jarvis" to wake it up
- Real-time weather via OpenWeatherMap
- Music playback via YouTube Music
- Top news headlines via NewsAPI
- System controls — volume, brightness, open apps and websites
- Date and time queries
- General AI conversation powered by Google Gemini 2.5 Flash
- Persistent memory — remembers your name, city, and last song
- Smart listening — stops recording when you stop speaking

---

## Project Structure

```
Jarvis-AI-Assistant/
├── Engine/
│   ├── speech.py          # Microphone input with voice activity detection
│   ├── tts.py             # Text-to-speech output
│   └── brain.py           # Gemini AI integration
├── core/
│   ├── intent_classifier.py   # Classifies user intent from text
│   ├── command_router.py      # Routes intent to correct command
│   └── memory.py              # Persistent JSON-based memory
├── commands/
│   ├── weather_command.py
│   ├── music_command.py
│   ├── datetime_command.py
│   ├── system_command.py
│   └── news_command.py
├── Tools/
│   ├── weather.py
│   ├── musiclibrary.py
│   ├── news.py
│   ├── jarvis_controls.py
│   └── datetime_utils.py
├── tests/
│   ├── test_intent_classifier.py
│   ├── test_memory.py
│   └── test_datetime_command.py
├── main.py
├── requirements.txt
└── .env
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sowhardya404/Jarvis-AI-Assistant.git
cd Jarvis-AI-Assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file in the project root

```
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
NEWSAPI_KEY=your_newsapi_key
```

### 4. Run Jarvis

```bash
python main.py
```

---

## Usage

| You say | Jarvis does |
|---|---|
| "Jarvis" | Wakes up and listens |
| "What's the weather in Kolkata" | Fetches live weather |
| "Play Blinding Lights" | Opens song on YouTube Music |
| "What's the time" | Tells current time |
| "Volume up" | Increases system volume |
| "Open YouTube" | Opens YouTube in browser |
| "What's in the news" | Reads top 5 headlines |
| "My name is Aryan" | Remembers your name |
| "Tell me a joke" | Responds via Gemini AI |
| "Sleep" | Goes back to standby |
| "Shutdown" | Exits the program |

---

## Running Tests

```bash
python -m pytest tests/ -v
```

---

## Tech Stack

- Python 3.14
- Google Gemini 2.5 Flash — AI responses
- SpeechRecognition + SoundDevice — voice input
- pyttsx4 — text to speech
- OpenWeatherMap API — weather
- YTMusicAPI — music
- NewsAPI — headlines
- screen-brightness-control — display control
- NirCmd — volume control

---
