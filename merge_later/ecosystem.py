import random

from merge_later.after_middle import Bear, Fish


class River:
    def __init__(self, size, bears_num, fish_num):
        self._elements = self.generate(size, bears_num, fish_num)

    @staticmethod
    def generate(size, bears_num, fish_num):
        lst = [None] * size
        indexes = random.sample(range(size), bears_num + fish_num)
        for i in indexes[:bears_num]:
            lst[i] = Bear("Bear")
        for i in indexes[bears_num:]:
            lst[i] = Fish("Fish")
        return lst

    def add(self, idx,, animal):
        empty_cell = [i for i, el in enumerate(self._elements) if el is None]
        if self._elements[idx] is None:
            self._elements[idx] = None
        else:
            if type(animal) == type(self._elements):
                pass

    def __str__(self):
        return "".join([" " if el is None else repr(el) for el in
                        self._elements])


if __name__ == '__main__':
    r = River(9, 1, 3)
    print(r)
