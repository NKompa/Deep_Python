MIN_YEAR = 1
MAX_YEAR = 9999


def is_leap_year(year: int) -> bool:
    """Function is_leap_year checks if the input year is leap
    >>> is_leap_year(2016)
    True
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def check_date(input_date: str) -> bool:
    """Function check_date answers if the input date exists or not within 1-9999 year
    >>> check_date('01.01.2022')
    True
    >>> check_date('29.02.2023')
    False
    """
    day, month, year = map(int, input_date.split('.'))
    if year < MIN_YEAR or year > MAX_YEAR:
        return False
    if month < 1 or month > 12:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2:
        if is_leap_year(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False

    if day < 1 or day > 31:
        return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)