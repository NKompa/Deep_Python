import os


def rename_files(new_name: str, num_digits: int, current_ext: str, new_ext: str, char_range: tuple) -> None:
    files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.' + current_ext)]

    for i, old_file in enumerate(files):
        old_name = os.path.splitext(old_file)[0]
        old_name = old_name[char_range[0]: char_range[1]]

        number = str(i + 1).zfill(num_digits)

        new_file_name = old_name + new_name + number + '.' + new_ext
        os.rename(old_file, new_file_name)


if __name__ == "__main__":
    rename_files('file', 2, 'txt', 'docx', (0, 3))