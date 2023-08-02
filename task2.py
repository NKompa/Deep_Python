from Exceptions import MyRectangleException


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        if self.width <= 0 or self.height <= 0:
            raise MyRectangleException(width, height)
        self.function_type = None

    def rectangle_perimeter(self):
        self.function_type = 'perimeter'
        return (self.width + self.height) * 2

    def rectangle_square(self):
        self.function_type = 'square'
        return self.width * self.height

    def __str__(self):
        if self.function_type == 'perimeter':
            return f'периметр = {self.rectangle_perimeter()}, ширина = {self.width}, высота = {self.height}'
        if self.function_type == 'square':
            return f'площадь = {self.rectangle_square()}, ширина = {self.width}, высота = {self.height}'
        else:
            return f'ширина = {self.width}, высота = {self.height}'


if __name__ == "__main__":
    r1 = Rectangle(20, -10)
    r1.rectangle_square()
    print(r1)