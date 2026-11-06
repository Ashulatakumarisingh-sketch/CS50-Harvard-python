from numb3rs import validate

def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_range():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False

def test_invalid_format():
    assert validate("google.com") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False
