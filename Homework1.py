import os
import json
import csv
import pickle


def get_directory_size(directory):
    total_size = 0
    for path, dirs, files in os.walk(directory):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            result = {
                "path": path,
                "type": "file",
                "size": size
            }
            results.append(result)
        for name in dirs:
            path = os.path.join(root, name)
            size = get_directory_size(path)
            result = {
                "path": path,
                "type": "directory",
                "size": size
            }
            results.append(result)
    return results


def save_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def save_to_csv(data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["path", "type", "size"])
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)


if __name__ == "__main__":
    directory = "D:\Documents\Обучение\IT\Python_files\Deep_Python_Seminars"
    results = traverse_directory(directory)
    save_to_json(results, "results.json")
    save_to_csv(results, "results.csv")
    save_to_pickle(results, "results.pickle")