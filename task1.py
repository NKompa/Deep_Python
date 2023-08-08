import argparse
import logging
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


parser = argparse.ArgumentParser()
parser.add_argument('--width', type=int, help='ширина прямоугольника')
parser.add_argument('--height', type=int, help='высота прямоугольника')
args = parser.parse_args()


logging.basicConfig(filename='log_new.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def run_rectangle(width, height):
    try:
        r = Rectangle(width, height)
        r.rectangle_square()
        logging.info(str(r))
    except MyRectangleException as e:
        error_message = str(e)
        logging.error(f"MyRectangleException: {error_message}")


if __name__ == "__main__":
    run_rectangle(args.width, args.height)