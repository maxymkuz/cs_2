import random

from animals import Bear, Fish


class River:
    def __init__(self, size, bears_num, fish_num):
        self._elements = self.generate(size, bears_num, fish_num)

    @staticmethod
    def generate(size, bears_num, fish_num):
        """
        Generates an starting map
        """
        lst = [None] * size
        indexes = random.sample(range(size), bears_num + fish_num)
        for i in indexes[:bears_num]:
            lst[i] = Fish()
        for i in indexes[bears_num:]:
            lst[i] = Bear()
        return lst

    @staticmethod
    def generate_moves(size):
        return [random.randint(-1, 1) for i in range(size)]

    @staticmethod
    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    def collide(self, first, second, colliding_index):
        """
        Compares two instances of animal and returns appropriate animal for
        the colliding cell first, and then for second cell
        """
        # Two similar animal case
        if first.name == second.name:
            child = type(first)()
            self.add_child(child, colliding_index)
            return second, first
        else:  # If there are different animals, the strongest type wins
            if first.name == 'B':
                return first, None
            elif second.name == 'B':
                return second, None

    def add_child(self, child, colliding_index):
        """
        Adds the children lefter than the colliding index if possible
        if not possible- add the child righter
        """
        for j in range(colliding_index - 1, -1, -1):
            # If we find a place for a child:
            if self._elements[j] is None:
                self._elements[j] = child
                return None
        # If not possible, then placing it righter
        for j in range(colliding_index, len(self._elements)):
            # If we find a place for a child:
            if self._elements[j] is None:
                self._elements[j] = child
                return None

    def move(self):
        """
        Main function that moves each animal exactly
        one postion in a random direction and handles collisions
        """
        # Generating random set of moves for a river:
        moves = self.generate_moves(len(self._elements))
        i = 0
        while i < len(self._elements):
            # In which direction does the current animal move
            current_move = moves[i]
            # Checking if in current cell there is an animal to move
            if self._elements[i] is None:
                i += 1
                continue

            # 1. If the animal moves forward:
            if current_move == 1:
                # Check if it is the last element:
                if i == len(self._elements) - 1:
                    i += 1
                    continue
                if self._elements[i + 1] is None:
                    self.swap(self._elements, i, i + 1)
                    i += 2
                # If current moves forward and the next animal backwards
                elif moves[i + 1] == -1:
                    self.swap(self._elements, i, i + 1)
                    i += 2
                # If the current animal collides with the next element:
                else:
                    try:
                        self._elements[i + 1], self._elements[i] = self.collide(self._elements[i], self._elements[i + 1], i)
                    except TypeError:  # This error is raised only in case
                        # if nothing is changed on the river, so do not pay
                        # attention on this
                        pass
                    finally:
                        i += 2

            # 2. If current animal moves backwards
            elif current_move == -1:
                # checking if it's the first element:
                if i == 0:
                    i += 1
                    continue
                if self._elements[i - 1] is None:
                    self.swap(self._elements, i - 1, i)
                    i += 2
                # If prev elem is an animal, we collide them
                else:
                    try:
                        self._elements[i - 1], self._elements[i]= self.collide(self._elements[i - 1], self._elements[i], i - 1)
                    except TypeError:  # This error is raised only in case
                        # if nothing is changed on the river, so do not pay
                        # attention on this
                        pass
                    finally:
                        i += 2
            else:  # if current_move == 0, do nothing
                i += 1
        print(self)

    def get_animal_num(self, animal_type):
        """
        Just returns the amount of alive animals
        """
        if animal_type == "Fish":
            return str(self).count("F")
        if animal_type == "Bear":
            return str(self).count("B")
        return None

    def __str__(self):
        return "".join(
            ["_" if el is None else el.name for el in self._elements])


if __name__ == '__main__':
    r = River(15, 3, 3)
    r.move()
    r.move()
    r.move()
    r.move()
    r.move()
    r.move()
    r.move()
    r.move()
    r.move()
    r.move()
