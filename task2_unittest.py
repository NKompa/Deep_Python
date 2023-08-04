import unittest
from task2_doctest import Circle
from Exceptions import MyRadiusException


class TestCircle(unittest.TestCase):
    def test_circle_creates(self):
        c1 = Circle(10)
        self.assertIsInstance(c1, Circle)

    def test_raise_exception(self):
        with self.assertRaises(MyRadiusException) as cm:
            Circle(0)
        self.assertEqual(str(cm.exception), 'Окружность с радиусом 0 не существует.')

    def test_circle_length(self):
        self.assertEqual(25.132741228718345, Circle(4).circle_length())

    def test_circle_square(self):
        self.assertEqual(254.46900494077323, Circle(9).circle_square())


if __name__ == "__main__":
    unittest.main(verbosity=2)