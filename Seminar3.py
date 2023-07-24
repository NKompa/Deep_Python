import json
import csv


def convert_csv(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        data_dict = json.load(file)
        data_list = []
        for level, user in data_dict.items():
            for user_id, name in user.items():
                data_list.append({'level': int(level), 'id': int(user_id), 'name': name})

    with open('task3.csv', 'w', encoding='utf-8') as c:
        csv_writer = csv.DictWriter(c, fieldnames=('level', 'id', 'name'))
        csv_writer.writeheader()
        csv_writer.writerows(data_list)


if __name__ == "__main__":
    convert_csv("task2.json")