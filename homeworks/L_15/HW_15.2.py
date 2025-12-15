class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        # Реалізація множення дробів.
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        # Реалізація додавання дробів.
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)

    def __sub__(self, other):
        # Реалізація віднімання дробів.
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)

    def __eq__(self, other):
        # Перевірка на рівність через перехресне множення.
        return self.a * other.b == other.a * self.b

    def __gt__(self, other):
        # Перевірка 'більше' через перехресне множення.
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        # Перевірка 'менше' через перехресне множення.
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Unit Test.
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'
assert f_d < f_c
assert f_d > f_e
assert f_a != f_b
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2
print('OK')