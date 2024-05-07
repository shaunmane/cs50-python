from twttr import shorten

def test_twitter():
    assert shorten("hello") == "hll"
    assert shorten("David") == "Dvd"
    assert shorten("jAke") == "jk"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"