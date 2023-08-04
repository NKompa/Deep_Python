import pytest
from task1_doctest import check_date, is_leap_year


def test_date_exists():
    assert check_date('01.01.2022') is True


def test_date_impossible():
    assert check_date('29.02.2023') is False


def test_leap_year():
    assert is_leap_year(2000) is True


def test_not_leap_year():
    assert is_leap_year(2001) is False


if __name__ == "__main__":
    pytest.main(['-vv'])
