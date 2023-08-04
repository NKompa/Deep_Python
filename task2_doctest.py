import math
from Exceptions import MyRadiusException


class Circle:
    def __init__(self, radius):
        """Method __init__ in class Circle checks input radius: if it's 0 or below 0 method should raise exception.
        >>> try:
        ...     Circle(0)
        ... except MyRadiusException as e:
        ...     str(e)
        'Окружность с радиусом 0 не существует.'
        >>> c = Circle(5)
        """
        self.radius = radius
        if radius <= 0:
            raise MyRadiusException(radius)

    def circle_length(self):
        """Method circle_length calculates the length of the circle with given radius.
        >>> Circle(4).circle_length()
        25.132741228718345
        """
        return 2 * math.pi * self.radius

    def circle_square(self):
        """Method circle_square calculates the square of the circle with given radius.
        >>> Circle(9).circle_square()
        254.46900494077323
        """
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
