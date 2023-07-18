import random
import string


def create_files(extension, min_name_length=6, max_name_length=30, min_bytes=256, max_bytes=4096, num_files=42):
    for _ in range(num_files):
        file_name = ''.join(
            random.choices(string.ascii_lowercase + string.digits, k=random.randint(min_name_length, max_name_length)))
        file_name += "." + extension

        file_size = random.randint(min_bytes, max_bytes)
        file_content = bytes(random.choices(range(256), k=file_size))

        with open(file_name, 'wb') as file:
            file.write(file_content)


if __name__ == "__main__":
    create_files("txt", min_name_length=5, max_name_length=10, min_bytes=512, max_bytes=2048, num_files=10)