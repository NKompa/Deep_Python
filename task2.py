class Archive:
    """Class Archive creates list of all inputs of numbers and texts."""
    __instance = None

    def __init__(self, num, text):
        self.num = num
        self.text = text

    def __new__(cls, *args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.num_list = []
            cls.__instance.text_list = []
        else:
            cls.__instance.num_list.append(cls.__instance.num)
            cls.__instance.text_list.append(cls.__instance.text)
        return cls.__instance

    def __str__(self):
        return f"Текст = {self.text}, число = {self.num}, архив текста = {self.text_list}, " \
               f"архив чисел = {self.num_list}"

    def __repr__(self):
        return f"Текст = {self.text}, число = {self.num}"


if __name__ == "__main__":
    print(Archive.__doc__)
    new_arch = Archive(1, 'test')
    print(new_arch)
    print(repr(new_arch))
    new_arch = Archive(2, 'new_test')
    print(new_arch)
    print(repr(new_arch))