from PS7.Numb3rs.numb3rs import validate

def test_correct_digits():
    assert validate("255.255.255.255") == True
    assert validate("0.255.255.255") == True
    assert validate("255.51.0.0") == True

def test_above():
    assert validate("512.512.512.512") == False
    assert validate("256.0.0.0") == False
    assert validate("255.300.255.255") == False
    assert validate("1.2.3.1000") == False


def test_words():
    assert validate("cat") == False
    assert validate("abc.222.231.0") == False

