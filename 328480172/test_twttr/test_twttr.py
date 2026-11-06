from twttr.twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert  shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("cs50 2026") == "cs50 2026"

def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
