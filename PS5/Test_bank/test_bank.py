import pytest
from bank import value


def test_hello():
    assert value("hello".casefold()) == 0
    assert value("hello, world".casefold()) == 0


def test_h():
    assert value("hey") == 20
    assert value("hi") == 20
    assert value("Howsit") == 20


def test_not_h():
    assert value("What") == 100
    assert value("whatsup") == 100
    assert value("where") == 100


