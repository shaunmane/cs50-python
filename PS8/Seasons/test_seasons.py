from seasons import get_date
import pytest

# tests the format of the string
def test_format():
    with pytest.raises(SystemExit):
        get_date("20-10-1995") == "Invalid date"
        get_date("2022/09/05") == "Invalid date"

# tests dates out of range
def test_range():
    with pytest.raises(SystemExit):
        get_date("2022-19-05") == "Invalid date"
        get_date("2022-10-3cd5") == "Invalid date"

# tests words
def test_error():
    with pytest.raises(SystemExit):
        get_date("Cat") == "Invalid date"
        get_date("1996bat") == "Invalid date"