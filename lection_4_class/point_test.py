from point import Point


if __name__ == '__main__':
    point = Point(1, 1)
    assert isinstance(point, Point)
    print("Methods: ", dir(point))
    print("Attributes: ", point.__dict__)
    print("There are no errors. Thank You!")