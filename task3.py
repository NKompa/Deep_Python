class Rectangle:
    """Class Rectangle performs operations with rectangle"""
    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def rectangle_perimeter(self):
        """Method rectangle_perimeter provides perimeter of rectangle"""
        return (self.width + self.height) * 2

    def rectangle_square(self):
        """Method rectangle_square provides square of rectangle"""
        return self.width * self.height

    def __add__(self, other):
        perimeter = self.rectangle_perimeter() + other.rectangle_perimeter()
        width = self.width + other.width
        height = (perimeter - width) / 2
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.rectangle_perimeter() < other.rectangle_perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.rectangle_perimeter() - other.rectangle_perimeter()
        height = (perimeter - width) / 2
        return Rectangle(width, height)

    def __str__(self):
        return f'периметр = {self.rectangle_perimeter()}, длина = {self.width}, высота = {self.height}'

    def __eq__(self, other):
        return self.rectangle_square() == other.rectangle_square()

    def __lt__(self, other):
        return self.rectangle_square() < other.rectangle_square()

    def __le__(self, other):
        return self.rectangle_square() <= other.rectangle_square()


if __name__ == "__main__":
    print(Rectangle.__doc__)
    r1 = Rectangle(20, 30)
    r2 = Rectangle(50)
    print(r1 + r2)
    print(r1 - r2)
    print(r1 == r2)
    print(r1 < r2)
    print(r1 <= r2)