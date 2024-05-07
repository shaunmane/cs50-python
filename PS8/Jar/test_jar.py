from jar import Jar
import pytest


def test_correct_init():
    jar = Jar()
    assert str(jar) == ''


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)

    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar(9)

    jar.deposit(6)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(10)

    with pytest.raises(ValueError):
        jar.deposit(-1)
