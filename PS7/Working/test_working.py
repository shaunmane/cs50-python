import pytest
from working import convert

def test_PM():
    assert convert("5:00 PM to 11:00 PM") == "17:00 to 23:00"
    assert convert("1:00 PM to 9:00 PM") == "13:00 to 21:00"

def test_AM():
    assert convert("5:00 AM to 11:00 AM") == "05:00 to 11:00"
    assert convert("1:00 AM to 8:00 AM") == "01:00 to 08:00"

def test_PM_to_AM():
    assert convert("6:00 PM to 11:00 AM") == "18:00 to 11:00"
    assert convert("11:00 PM to 9:00 AM") == "23:00 to 09:00"

def test_AM_to_PM():
    assert convert("5:00 AM to 1:00 PM") == "05:00 to 13:00"
    assert convert("11:00 AM to 4:00 PM") == "11:00 to 16:00"

def test_no_minutes():
    assert convert("8 AM to 4 PM") == "08:00 to 16:00"
    assert convert("12 PM to 8 PM") == "12:00 to 20:00"

def test_12():
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12:00 AM to 1:00 PM") == "00:00 to 13:00"

def test_ValueError():
    with pytest.raises(ValueError):
        convert("09:00 AM - 7:00 PM")
    with pytest.raises(ValueError):
        convert("09:70 AM to 7:00 PM")

