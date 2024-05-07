from plates import is_valid

def test_length():
    assert is_valid("a") == False
    assert is_valid("plat123") == False
    assert is_valid("CS50") == True


def test_startAlphabets():
    assert is_valid("AB") == True
    assert is_valid("B223") == False
    assert is_valid("B7") == False


def test_numbers():
    assert is_valid("sk1n") == False
    assert is_valid("PLAT3S") == False
    assert is_valid("BB001") == False
    assert is_valid("ll100") == True


def test_punct():
    assert is_valid("C!S50") == False
    assert is_valid("PI3.14") == False
    assert is_valid("AB 13 CD") == False


