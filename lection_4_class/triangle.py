import point


class Triangle:
    """Represents an triangle"""

    def __init__(self, p1, p2, p3):
        """Initialize"""
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def is_triangle(self):
        """ (Triangle) -> bool
        Return True if it's a triangle"""
        distances = sorted([self.dis(self.p1, self.p2),
                            self.dis(self.p2, self.p3),
                            self.dis(self.p3, self.p1)])
        return True if distances[0] + distances[1] > distances[2] else False

    def perimeter(self):
        """ (Triangle) -> float
        Return the perimeter"""
        return sum([self.dis(self.p1, self.p2), self.dis(self.p2, self.p3),
                    self.dis(self.p3, self.p1)]) \
            if self.is_triangle() else False

    def area(self):
        """ (Triangle) -> float
        Return the area of a triangle"""
        p = self.perimeter() / 2
        return (p * (p - self.dis(self.p1, self.p2)) *
                (p - self.dis(self.p2, self.p3)) *
                (p - self.dis(self.p1, self.p3))) ** 0.5

    @staticmethod
    def dis(a, b):
        """ (Point, Point) -> float
        Returns the distances between Point a and b"""
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5



# Aggregation - сукупність aggregate objects can exist independently