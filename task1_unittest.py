import unittest
from task1_doctest import check_date, is_leap_year


class TestDate(unittest.TestCase):
    def test_date_exists(self):
        self.assertEqual(True, check_date('01.01.2022'))

    def test_date_impossible(self):
        self.assertEqual(False, check_date('29.02.2023'))

    def test_leap_year(self):
        self.assertEqual(True, is_leap_year(2000))

    def tes_not_leap_year(self):
        self.assertEqual(False, is_leap_year(2001))


if __name__ == "__main__":
    unittest.main(verbosity=2)