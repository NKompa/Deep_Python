_result = dict()


def riddle_guess(text: str, options: list, tries: int) -> int:
    print(f"Добрый день! Ваша загадка на сегодня: {text}")
    for i in range(1, tries+1):
        answer = input(f"Попытка №{i}. Введите ответ: ")
        if answer in options:
            print(f"Вы угадали!")
            return i
        else:
            print("Ответ неверный!")
    print("Вы не угадали:(")
    return 0


def all_riddles(riddle_dict: dict[str, list[str]], count: int = 3) -> None:
    for key, value in riddle_dict.items():
        res = riddle_guess(key, value, count)
        save_result(key, res)
        print(f"Exit code: {res}")
    print_result()


def save_result(text: str, count: int) -> None:
    _result.update({text: count})


def print_result():
    print_res = (f"Загадка - {key} - отгадана за {value} попытки." if value > 0
                 else f"Загадка - {key} - не отгадана." for key, value in _result.items())
    print("Статистика: ")
    print("\n".join(print_res))


if __name__ == "__main__":
    riddles_answers = {
        "Кто от дедушки ушел?": ["бабушка", "волк", "колобок"],
        "Не лает, не кусает, в дом не пускает": ["замок", "замочек"],
        "Зимой и летом одним цветом": ["елка", "ель"]
    }
    all_riddles(riddles_answers)