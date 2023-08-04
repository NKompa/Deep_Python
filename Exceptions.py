class MyExceptions(Exception):
    pass


class MyRadiusException(MyExceptions):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'Окружность с радиусом {self.radius} не существует.'


class MyRectangleException(MyExceptions):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Прямоугольник с шириной {self.width} и высотой {self.height} не существует.'