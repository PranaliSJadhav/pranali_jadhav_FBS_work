class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return ComplexNumber(r, i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return ComplexNumber(r, i)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __del__(self):
        pass


# Object creation
c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, 3)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
