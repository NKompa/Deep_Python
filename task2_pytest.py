import pytest
from task2_doctest import Circle
from Exceptions import MyRadiusException


def test_circle_creates():
    c1 = Circle(10)
    assert isinstance(c1, Circle)


def test_raise_exception():
    with pytest.raises(MyRadiusException) as cm:
        Circle(0)
    assert str(cm.value) == 'Окружность с радиусом 0 не существует.'


def test_circle_length():
    assert 25.132741228718345 == Circle(4).circle_length()


def test_circle_square():
    assert 254.46900494077323 == Circle(9).circle_square()


if __name__ == "__main__":
    pytest.main(['-vv'])
