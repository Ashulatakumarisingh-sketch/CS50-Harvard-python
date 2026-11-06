import pytest
from um import count


def test_standalone_and_case():
    assert count("um") == 1
    assert count("Um, thanks for the help.") == 1
    assert count("UM... what did you say? Um...") == 2


def test_inside_words():
    assert count("yummy food") == 0
    assert count("an umbrella in the rain") == 0
    assert count("instruments like drums") == 0


def test_with_punctuation():
    assert count("um?") == 1
    assert count("Hello, um, world!") == 1
    assert count("...um...") == 1
