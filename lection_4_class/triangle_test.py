from triangle import Triangle
from point import Point


if __name__ == '__main__':
    triangle = Triangle(Point(1, 1), Point(3, 1), Point(2, 3))
    print(triangle.perimeter())
    assert isinstance(triangle, Triangle)
    print("Methods: ", dir(triangle))
    print("Attributes: ", triangle.__dict__)
    assert triangle.area() == 2.0
    print("There are no errors. Thank You!")