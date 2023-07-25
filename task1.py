import csv
import os
import json
from math import sqrt
from typing import Callable
import random


def create_csv(filename, num_lines):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_lines):
            writer.writerow([random.randint(1, 100) for _ in range(3)])


def results_to_json(func: Callable):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if not os.path.isfile('results.json'):
            data = []
        else:
            with open('results.json', 'r') as jsonfile:
                data = json.load(jsonfile)

        data.append({
            'a': a,
            'b': b,
            'c': c,
            'result': result
        })

        with open('results.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4, separators=(',', ': '))

    return wrapper


def root_quadratic_deco(func: Callable):
    def wrapper(filename):
        results = []

        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                results.append({
                    'a': a,
                    'b': b,
                    'c': c,
                    'result': result
                })
        return results

    return wrapper


@root_quadratic_deco
@results_to_json
def root_quadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "No roots"
    elif discriminant == 0:
        root1 = -b / (2 * a)
        return root1
    else:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return [root1, root2]


if __name__ == "__main__":
    create_csv('random_numbers.csv', 100)
    root_quadratic('random_numbers.csv')
