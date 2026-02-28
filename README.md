# JARVIS — Desktop AI Voice Assistant

JARVIS is a modular AI-powered desktop voice assistant built using Python.
It listens to voice commands, understands user intent, executes system tasks, and falls back to generative AI when needed.

 JARVIS demonstrates:

- AI integration
- Voice interaction
- Command routing architecture
- Memory persistence
- System automation

## Key Features

### Voice Interaction

- Wake word activation ("Jarvis")
- Real-time speech recognition
- Natural conversational responses
- Hands-free desktop interaction

### Intelligent AI Assistant

- Generative AI powered conversation engine
- Context-aware responses
- AI fallback when commands are unknown

### Desktop Automation

- Open applications and websites
- Volume and brightness control
- File & folder access
- System shutdown and control operations

### Smart Information Services

- Real-time weather updates via API integration
- News Updates via API intergration
- Online information retrieval
- Fast web navigation

### Music Control

- Voice-based music playback
- Smart command handling
- Session memory for previous actions

### Persistent Memory System

Stores user preferences including:

- User name
- Default city
- Last command history

## Tech Stack

### Programming Language

Python

### AI & NLP

- Google Gemini API (Generative AI)
- SpeechRecognition
- Natural Language Intent Classification

### Automation

- Volume Control Automation
- Screen Brightness Management
- Application Launch Automation (Notepad, Calculator)
- File & Folder Navigation via Voice Commands

### API Integrations

- OpenWeather API — Real-time weather data retrieval
- YouTube Music API (YTMusic) — Voice-controlled music playback
- NewsAPI — Live news headline aggregation and updates

### Software Engineering

- Object-Oriented Programming
- Modular Design

## Architecture

```text
User Voice
   ↓
Speech Recognition
   ↓
Intent Classifier
   ↓
Command Router
   ↓
Specific Command Module
   ↓
AI Fallback (Gemini)
   ↓
Text To Speech Response

Main execution loop located in main.py
```

## Project Structure

```text
JARVIS/
│
├── main.py                # Entry point
│
├── Engine/
│   ├── speech.py          # Voice input listener
│   ├── tts.py             # Text-to-speech output
│   └── brain.py           # Gemini AI integration
│
├── core/
│   ├── intent_classifier.py
│   ├── command_router.py
│   └── memory.py
│
├── commands/
│   ├── datetime_command.py
│   ├── music_command.py
│   ├── weather_command.py
│   └── system_command.py
│
└── Tools/
    ├── jarvis_controls.py
    ├── weather.py
    ├── musiclibrary.py
    └── datetime_utils.py
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Author

Sowhardya Biswas
B.Tech Computer Science Engineering
AI • Data Analytics • Software Engineering.

## License

This project is for educational purposes.
