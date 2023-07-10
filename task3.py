import random
from task2 import check_queens


def generate_position():
    max_position = 8
    position = []
    for i in range(1, max_position + 1):
        position.append((i, random.randint(1, max_position)))
    return position


def find_good_position():
    count = 0
    while count < 4:
        new_position = generate_position()
        if check_queens(new_position):
            print(new_position)
            count += 1


if __name__ == "__main__":
    find_good_position()
