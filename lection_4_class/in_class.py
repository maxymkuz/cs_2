from dataclasses import dataclass

@dataclass()
class Markets:
    name: str
    area: int
    categories: list


class Student:
    def __init__(self):
        self.name = ""
        self.age = 0

    def __str__(self):
        return self.name + " age: " + str(self.age)

    def is_old(self):
        if self.age < 12:
            return "Young"
        elif self.age < 20:
            return "Fresh"
        else:
            return "Old"

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_to_origin(self):
        return ((self.x)**2 + self.y**2)**0.5


s = Point(1, 1)
print(s.distance_to_origin())
if __name__ == '__main__':
    s = Student()
    s.name = "Max"
    s.age = 11
    print(s.is_old())