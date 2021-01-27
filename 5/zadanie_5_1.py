class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def conjugate(self):
        return Complex(self.r, -self.i)

    def add(self, complex_b):
        return Complex(self.r + complex_b.r, self.i + complex_b.i)

    def sub(self, complex_b):
        return Complex(self.r - complex_b.r, self.i - complex_b.i)

    def mod(self):
        return (self.r**2 + self.i**2)**0.5

    def mult(self, complex_b):
        return Complex(self.r * complex_b.r - self.i * complex_b.i, self.r * complex_b.i + self.i * complex_b.r)

