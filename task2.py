import json


class JSONConverter:
    def __init__(self, path):
        self.path = path

    def convert_to_json(self):
        dict1 = {}
        with open(self.path, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip('\n')
                number, name = line.split('|')
                dict1[name.capitalize()] = float(number)
        print(dict1)
        with open('task2.json', 'w', encoding='utf-8') as j:
            json.dump(dict1, j, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    converter = JSONConverter(r'D:\Documents\Обучение\IT\Python_files\Deep_Python_Seminars\Seminar_7\results.txt')
    converter.convert_to_json()