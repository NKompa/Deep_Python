import math
from Exceptions import MyRadiusException


class Circle:
    def __init__(self, radius):
        self.radius = radius
        if radius <= 0:
            raise MyRadiusException(radius)

    def circle_length(self):
        return 2 * math.pi * self.radius

    def circle_square(self):
        return math.pi * self.radius**2


if __name__ == "__main__":
    c1 = Circle(-5)
    print(f'{c1.circle_length()}')
    print(f'{c1.circle_square()}')