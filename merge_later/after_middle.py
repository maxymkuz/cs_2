import random


class Animal:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name


class Bear(Animal):
    def __init__(self, name):
        super().__init__(name)


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)


print(random.sample([1, 2, 3, 4, 5], 2))