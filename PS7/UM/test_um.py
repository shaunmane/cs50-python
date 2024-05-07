import pytest
from um import count

def test_case():
    assert count("Um") == 1
    assert count("um") == 1

def test_multiple():
    assert count("Um, thanks, um") == 2
    assert count("um, um, um") == 3

def test_inWords():
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
    assert count("Um, thanks, um, regular expressions make sense now.") == 2