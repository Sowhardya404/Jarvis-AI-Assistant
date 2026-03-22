import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.intent_classifier import IntentClassifier

classifier = IntentClassifier()

def test_weather_intent():
    assert classifier.classify("what's the weather in kolkata") == "weather"

def test_datetime_time_intent():
    assert classifier.classify("what is the time") == "datetime"

def test_datetime_date_intent():
    assert classifier.classify("what is the date today") == "datetime"

def test_music_intent():
    assert classifier.classify("play shape of you") == "music"

def test_system_volume_intent():
    assert classifier.classify("volume up") == "system"

def test_system_open_intent():
    assert classifier.classify("open youtube") == "system"

def test_set_name_intent():
    assert classifier.classify("my name is aryan") == "set_name"

def test_reset_memory_intent():
    assert classifier.classify("reset memory") == "reset_memory"

def test_news_intent():
    assert classifier.classify("show me the news") == "news"

def test_ai_fallback_intent():
    assert classifier.classify("tell me a joke") == "ai_fallback"