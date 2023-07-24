import json


def convert_to_json(path: str) -> None:
    dict1 = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip('\n')
            number, name = line.split('|')
            dict1[name.capitalize()] = float(number)
    print(dict1)
    with open('task1.json', 'w', encoding='utf-8') as j:
        json.dump(dict1, j, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    convert_to_json(r'D:\Documents\Обучение\IT\Python_files\Deep_Python_Seminars\Seminar_7\results.txt')
