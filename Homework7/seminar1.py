from random import randint, uniform
MAX_NUM = 1000
MIN_NUM = -1000


def random_numbers(num_str: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_str):
            f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == "__main__":
    random_numbers(7, 'numbers.txt')