from random import random


class Animal:
    def __init__(self, name):
        self.name = name
        self.male = True if random() > 0.5 else False
        self.power = 10 * random()

    def __getitem__(self, y=[]):
        return self

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Bear(Animal):
    def __init__(self):
        super().__init__('B')


class Fish(Animal):
    def __init__(self):
        super().__init__("F")


if __name__ == '__main__':
    f = Fish()
    arr = [f, Bear()]
    arr[0], arr[1] = f, f
    print(arr)