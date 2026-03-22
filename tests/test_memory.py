import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from core.memory import Memory

@pytest.fixture
def memory(tmp_path):
    # Uses a temporary file so it never touches your real memory.json
    return Memory(filename=str(tmp_path / "test_memory.json"))

def test_save_and_get(memory):
    memory.save("user_name", "Sowhardya")
    assert memory.get("user_name") == "Sowhardya"

def test_get_missing_key_returns_none(memory):
    assert memory.get("nonexistent_key") is None

def test_overwrite_value(memory):
    memory.save("default_city", "Kolkata")
    memory.save("default_city", "Delhi")
    assert memory.get("default_city") == "Delhi"

def test_save_none_value(memory):
    memory.save("last_song", None)
    assert memory.get("last_song") is None  