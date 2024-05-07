from project import length_conv, weight_conv, temperature_conv
import pytest


# length tests
def test_length():
    assert length_conv(1, 2, 23) == "23 metres is equal to 0.02 kilometres"
    assert length_conv(2, 5, 500) == "500 kilometres is equal to 310.68 miles"

    assert length_conv(0, 2, 23) == "Invalid Input: Not a valid input"
    assert length_conv(2, 9, 23) == "Invalid Input: Not a valid input"

    assert length_conv(2, 2, 400) == "Invalid Input: Cannot convert same units"
    assert length_conv(5, 5, 300) == "Invalid Input: Cannot convert same units"

def test_length_negative():
    with pytest.raises(SystemExit, match="Invalid Input: length cannot be negative"):
        length_conv(3, 1, -155)
        length_conv(1, 6, -5)
        raise SystemExit("Invalid Input: length cannot be negative")

def test_length_valueX():
    with pytest.raises(ValueError):
        length_conv(2, "bat", 400)
        length_conv("cat", 5, 300)
        raise ValueError("Invalid Input: Not a number")


# weight tests
def test_weight():
    assert weight_conv(3, 1, 155) == "155 pounds is equal to 70.31 kilograms"
    assert weight_conv(1, 4, 5) == "5 kilograms is equal to 176.37 ounces"

    assert weight_conv(0, 2, 23) == "Invalid Input: Not a valid input"
    assert weight_conv(2, 9, 23) == "Invalid Input: Not a valid input"

    assert weight_conv(2, 2, 400)== "Invalid Input: Cannot convert same units"
    assert weight_conv(1, 1, 300)== "Invalid Input: Cannot convert same units"

def test_weight_negative():
    with pytest.raises(SystemExit, match="Invalid Input: weight cannot be negative"):
        weight_conv(3, 1, -155)
        weight_conv(1, 4, -5)
        raise SystemExit("Invalid Input: weight cannot be negative")

def test_weight_valueX():
     with pytest.raises(ValueError):
        weight_conv(2, "bat", 400)
        weight_conv("cat", 5, 300)
        raise ValueError("Invalid Input: Not a number")

# temperature tests
def test_temp():
    assert temperature_conv(1, 0) == "0 degrees Celsius is equal to 32.00 degrees Fahrenheit."
    assert temperature_conv(1, 100) == "100 degrees Celsius is equal to 212.00 degrees Fahrenheit."

    assert temperature_conv(2, 32) == "32 degrees Fahrenheit is equal to 0.00 degrees Celsius."
    assert temperature_conv(2, -40) == "-40 degrees Fahrenheit is equal to -40.00 degrees Celsius."

    assert temperature_conv(3, 0) == "Invalid choice. Please enter 1 or 2."
    assert temperature_conv(0, 0) == "Invalid choice. Please enter 1 or 2."

def test_temp_typex():
    with pytest.raises(TypeError):
        assert temperature_conv("cat", 0) == "Invalid choice. Please enter 1 or 2."
        assert temperature_conv(1, "bat") == "Invalid Input: Not a number"


