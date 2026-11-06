import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    custom_jar = Jar(5)
    assert custom_jar.capacity == 5
    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(6)
