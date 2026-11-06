import pytest
from seasons import check_date, convert_to_words

def test_check_date():
    with pytest.raises(ValueError):
        check_date("January 1, 2000")
    with pytest.raises(ValueError):
        check_date("2000-13-01")
    with pytest.raises(ValueError):
        check_date("2000-12-32")


def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_words(1440) == "One thousand, four hundred forty minutes"
