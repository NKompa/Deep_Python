import json
import csv


class CSVConverter:
    def __init__(self, path):
        self.path = path

    def convert_csv(self):
        with open(self.path, 'r', encoding='utf-8') as file:
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
    converter = CSVConverter("task3.json")
    converter.convert_csv()
