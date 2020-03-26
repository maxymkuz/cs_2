class SamePointError(Exception):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Point:
    def __init__(self, x, y):
        """
        Represents a point with x and y axis positions
        """
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, lst_points):
        """
        Represents a line in a f(x) = ax + b way
        if user inputs the same points, raises SamePointError
        """
        p1 = lst_points[0]
        p2 = lst_points[1]
        if p1 == p2:
            raise SamePointError(p1, p2)
        self.b = 0.0
        self.a = 0.0
        self.vertical = False
        self.get_coefficients(p1, p2)

    def get_coefficients(self, p1, p2):
        """
        Computes and assigns the coefficients of a line
        """
        if p2.x == p1.x:
            self.b = p1.x
            self.a = - 1.0
            self.vertical = True
        else:
            self.a = (p2.y - p1.y)/(p2.x - p1.x)
            self.b = p1.y - self.a * p1.x

    def __str__(self):
        y = "0" if self.vertical else "y"
        return f"{self.a} * x + {self.b} = {y}"

    def __eq__(self, other):
        """ Returns True if lines are similar"""
        if self.a == other.a and self.b == other.b and self.vertical == \
                other.vertical:
            return True
        return False

    def intersect(self, other):
        """
        This method returns False if two lines from argument
        don't have a point of intersection, self if they have infinite
        number of points, or point of intersection otherwise
        """
        # Vertical line(s) case:
        if self.vertical and other.vertical:
            if self.b != other.b:
                return False
            return self
        elif self.vertical:
            x = self.b
            y = x * other.a + other.b
            return Point(x, y)
        elif other.vertical:
            x = other.b
            y = x * self.a + self.b
            return Point(x, y)
        # Usual case(no vertical)
        if self.a == other.a:
            if self.b != other.b:
                # Lines do not intersect
                return False
            # Lines match each other:
            return self
        x = (other.b - self.b)/(self.a - other.a)
        y = self.a * x + self.b
        return Point(x, y)
