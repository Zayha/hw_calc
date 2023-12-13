class Calculator:
    def __init__(self, a: int, b: int):
        if isinstance(a, int):
            self._a = a
        else:
            raise ValueError("Передаваемая переменная должна иметь тип integer")
        if isinstance(b, int):
            self._b = b
        else:
            raise ValueError("Передаваемая переменная должна иметь тип integer")

    def __str__(self):
        return f"a = {self._a}, b = {self._b}"

    @property
    def addition(self):
        return self._a + self._b

    @property
    def subtraction(self):
        return self._a - self._b

    @property
    def multiplication(self):
        return self._a * self._b

    @property
    def division(self):
        if self._b == 0:
            raise ZeroDivisionError("На ноль делить нельзя")
        else:
            return self._a / self._b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b
