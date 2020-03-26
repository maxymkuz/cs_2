class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def degree(self):
        """ Returns the degree of a
        given polynom"""
        for i in range(len(self.coeffs)):
            if self.coeffs[i] != 0:
                return len(self.coeffs[i:]) - 1
        return 0

    def coeff(self, power):
        """ Returns the coefficient for x**i"""
        if len(self.coeffs) >= power >= 0:
            return self.coeffs[len(self.coeffs) - 1 - power]

    def evalAt(self, x):
        """ returns the polynomial evaluated
         at that value of x"""
        l = len(self.coeffs)
        return sum([self.coeffs[i] * x ** abs(i - l + 1)
                    for i in range(l - 1, -1, -1)])

    def scaled(self, scaling_factor):
        """ Scales the equasion
        by a given scaling factor"""
        return Polynomial([scaling_factor * i for i in self.coeffs])

    def derivative(self):
        return Polynomial([self.coeffs[i] * (len(self.coeffs) - i - 1)
                           for i in range(len(self.coeffs))][:-1])

    def addPolynomial(self, other):
        """ We can add polynomials together, which will add the
        coefficients of any terms with the same
        degree, and return a new polynomial"""
        if not isinstance(other, Polynomial):
            return None
        x = self.coeffs[::-1]
        y = other.coeffs[::-1]
        res = [sum(pair) for pair in zip(x, y)]
        res += x[min(len(x), len(y)):]
        res += y[min(len(x), len(y)):]
        return Polynomial(res[::-1])

    def multiplyPolynomial(self, other):
        """ lastly, we can multiple polynomials together,
         which will multiply the oefficients of two polynomials
         and return a new polynomial with the
         correct coefficients."""
        if not isinstance(other, Polynomial):
            return None
        res = [0 for i in range(len(self.coeffs + other.coeffs) - 1)]
        for i in range(len(self.coeffs) - 1, -1, -1):
            for j in range(len(other.coeffs) - 1, -1, -1):
                res[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(res)

    def __eq__(self, other):
        """ Makes an equasion and
        returns True if equal"""
        if isinstance(other, int):
            if len(self.coeffs) == 1 and self.coeffs[0] == other:
                return True
        elif isinstance(other, Polynomial):
            min_len = min(len(self.coeffs), len(other.coeffs))
            for i in range(1, min_len + 1):
                if self.coeffs[-i] != other.coeffs[-i]:
                    return False
            min_len = -1 if min_len == 0 else min_len
            if list(filter(lambda e: e != 0, self.coeffs[:-min_len])) == list(
                    filter(lambda e: e != 0, other.coeffs[:-min_len])):
                return True
        return False

    def __str__(self):
        return f"Polynomial(coeffs={self.coeffs})"

    def __hash__(self):
        return 1


class Quadratic(Polynomial):
    """ It's as the usual polynom but it is
    an quadatic formula"""

    def __init__(self, coeffs):
        """ Initializes and also checks for normal values"""
        if isinstance(coeffs, list) and len(coeffs) == 3 and coeffs[0] != 0:
            super().__init__(coeffs)
            self.a = self.coeffs[0]
            self.b = self.coeffs[1]
            self.c = self.coeffs[2]
        else:
            raise ValueError

    def __str__(self):
        return f"Quadratic(a={self.a}, b={self.b}, c={self.c})"

    def discriminant(self):
        """ Calculates the discriminant value"""
        return self.b ** 2 - 4 * self.a * self.c

    def numberOfRealRoots(self):
        """ REturns number of real roots"""
        if self.discriminant() > 0:
            return 2
        return 1 if self.discriminant() == 0 else 0

    def getRealRoots(self):
        """ Returns a list of real roots of quadratic"""
        if self.numberOfRealRoots() == 0:
            return []
        res = [(-self.b + self.discriminant() ** 0.5) / 2,
               (-self.b - self.discriminant() ** 0.5) / 2]
        return sorted(list(set(res)))


