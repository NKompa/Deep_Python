import json
import os
from random import randint
from typing import Callable


def check_params(func: Callable):
    min_num = 1
    max_num = 100
    min_try = 1
    max_try = 10

    def wrapper(number: int, tries: int):
        if number not in range(min_num, max_num + 1):
            number = randint(min_num, max_num)
        if tries not in range(min_try, max_try + 1):
            tries = randint(min_try, max_try)
        result = func(number, tries)
        return result

    return wrapper


def logger(func: Callable):
    file_name = f"{func.__name__}.json"
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
    else:
        data = []

    def wrapper(*args, **kwargs):
        json_dict = {"args": args, **kwargs}
        result = func(*args, **kwargs)
        json_dict["result"] = result
        data.append(json_dict)

        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        return result

    return wrapper


def count_func(num: int = 1):
    def deco(func: Callable):
        results = []

        def wrapper(*args, **kwargs):
            for _ in range(num):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return deco


@count_func(3)
@check_params
@logger
def guess_number(number: int, tries: int):
    for i in range(1, tries + 1):
        print(f"Попытка № {i}")
        input_num = int(input('Введите число: '))
        if input_num == number:
            print('Вы угадали!')
            return 'Вы угадали!'
        elif input_num < number:
            print('Слишком мало')
        elif input_num > number:
            print('Слишком много')
    print('Вы не угадали!')
    return "Вы не угадали!"


if __name__ == "__main__":
    game = guess_number(20, 3)
    print(game)