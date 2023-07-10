from sys import argv

MIN_YEAR = 1
MAX_YEAR = 9999


def _is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def check_date(input_date: str) -> bool:
    day, month, year = map(int, input_date.split('.'))
    if year < MIN_YEAR or year > MAX_YEAR:
        return False
    if month < 1 or month > 12:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    if month == 2:
        if _is_leap_year(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False

    if day < 1 or day > 31:
        return False

    return True


if __name__ == "__main__":
    print(check_date(argv[1]))