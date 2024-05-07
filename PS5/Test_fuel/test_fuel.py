import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75

def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_per():
    assert gauge(33) == "33%"
    assert gauge(67) == "67%"

def test_convert_errVal():
    with pytest.raises(ValueError):
        convert("cat/bat")

def test_convert_err_Type():
    with pytest.raises(TypeError):
        convert("cat"/"bat")

def test_convert_err():
    with pytest.raises(ZeroDivisionError):
        convert(100/0)



