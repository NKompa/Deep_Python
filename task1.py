class Animal:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        pass


class Fish(Animal):
    LEVEL1 = 10
    LEVEL2 = 50

    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def get_info(self):
        if self.speed < self.LEVEL1:
            return 'Slow fish'
        elif self.speed in range(self.LEVEL1, self.LEVEL2 + 1):
            return 'Fast fish'
        else:
            return 'Super fast fish'


class Cat(Animal):
    LEVEL1 = 10
    LEVEL2 = 50

    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def get_info(self):
        if self.weight < self.LEVEL1:
            return 'Small cat'
        elif self.weight in range(self.LEVEL1, self.LEVEL2 + 1):
            return 'Medium cat'
        else:
            return 'Big cat'


class Factory:
    def __init__(self, animal_type, name, **kwargs):
        self.animal_type = animal_type
        self.name = name
        self.kwargs = kwargs

    def create_animal(self):
        if self.animal_type == "Fish":
            return Fish(self.name, **self.kwargs)
        elif self.animal_type == "Cat":
            return Cat(self.name, **self.kwargs)


if __name__ == "__main__":
    fish1 = Factory("Fish", name="Nemo", speed=20).create_animal()
    print(f'{fish1.name} - {fish1.get_info()}')

    cat1 = Factory("Cat", name="Garfield", weight=55).create_animal()
    print(f'{cat1.name} - {cat1.get_info()}')
