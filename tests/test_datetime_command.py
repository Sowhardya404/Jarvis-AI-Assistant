import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from commands.datetime_command import DateTimeCommand

cmd = DateTimeCommand()

def test_returns_time():
    result = cmd.execute("what is the time")
    assert "time is" in result.lower()

def test_returns_date():
    result = cmd.execute("what is the date")
    assert "today is" in result.lower()

def test_returns_date_and_time():
    result = cmd.execute("what is the date and time")
    assert "today is" in result.lower()
    assert "time is" in result.lower()

