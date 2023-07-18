from random import choice, randint

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
MIN_LEN = 4
MAX_LEN = 7


def create_name(num_names: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_names):
            name = ''.join(choice(VOWELS) if i in (1, 4, 6) else choice(CONSONANTS)
                           for i in range(randint(MIN_LEN, MAX_LEN)))
            f.write(name.capitalize() + '\n')


if __name__ == "__main__":
    create_name(10, "names.txt")