from time import time


class MyString(str):
    """Class MyString provides additional info about str - author and time."""
    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        print(f'Создал класс {cls}')
        return instance

    def __str__(self):
        return f'Автор строки - {self.author}, время: {self.time}'

    def __repr__(self):
        return f'str.author={self.author}, str.time={self.time}'


if __name__ == "__main__":
    print(MyString.__doc__)
    new_str = MyString('Hi everybody', 'Mike')
    print(new_str)
    print(repr(new_str))