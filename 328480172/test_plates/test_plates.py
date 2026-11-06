
from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("cs50") == True

def test_beginning_letters():
    assert is_valid("C50") == False
    assert is_valid("50CS") == False

def test_length():
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_numbers_placement():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False

