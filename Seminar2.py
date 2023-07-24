import os
import json


def add_user(filename):
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            users = json.load(file)
    else:
        users = {str(i): {} for i in range(1, 8)}

    while True:
        name = input("Введите ваше имя (или 'q' для выхода): ")
        if name.lower() == 'q':
            break

        user_id = input("Введите ваш ID: ")
        access_level = input("Введите ваш уровень доступа (1-7): ")

        all_ids = [v for level in users.values() for v in level.keys()]

        if user_id not in all_ids:
            if access_level in users:
                users[access_level][user_id] = name
            else:
                print(f"Уровень доступа {access_level} не существует.")

        else:
            print("Данный ID уже существует.")

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    add_user("task2.json")