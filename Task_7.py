class ComplexNumbers:
    def __init__(self, real, imag):
        self.complex_number = complex(real, imag)

    def __str__(self):
        return f'{self.complex_number}'

    def __add__(self, other):
        result = self.complex_number + other.complex_number
        return ComplexNumbers(result.real, result.imag)

    def __mul__(self, other):
        result = self.complex_number * other.complex_number
        return ComplexNumbers(result.real, result.imag)


x = ComplexNumbers(1, -1)
y = ComplexNumbers(2, 2)
z = x + y
w = x * y
print(z, w)
