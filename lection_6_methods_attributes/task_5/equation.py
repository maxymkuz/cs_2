class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __str__(self):
        return f"Polynomial(coeffs={self.coeffs})"

    def degree(self):
        """ Returns the degree of a
        given polynom"""
        for i in range(len(self.coeffs)):
            if i != 0:
                return len(self.coeffs[i:])
        return 0

    def coeff(self, power):
        """ Returns the coefficient for x**i"""
        if len(self.coeffs) >= power >= 0:
            return self.coeffs[len(self.coeffs) - 1 - power]

    def evalAt(self, x):
        """ returns the polynomial evaluated
         at that value of x"""
        l = len(self.coeffs)
        return sum([self.coeffs[i] * x ** abs(i - l + 1) for i in range(l - 1,
                                                                        -1,
                                                                        -1)])
        # res = sum([reversed(self.coeffs)[i] * x ** i for i in range(len(
        #     self.coeffs)
        #                                                             - 1, -1,
        #                                                             -1)])

p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
assert (p1.degree() == 2)

# p.coeff(i) returns the coefficient for x**i
assert (p1.coeff(0) == 5)
assert (p1.coeff(1) == -3)
assert (p1.coeff(2) == 2)
assert (p1.evalAt(0) == 5)
assert (p1.evalAt(2) == 7)
