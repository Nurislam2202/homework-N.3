class Calculator:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.a + other.a)
        return Calculator(self.a + other)

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.a + other.a)
        return Calculator(self.a + other)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.a + other.a)
        return Calculator(self.a + other)

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            if other.a == 0:
                raise ZeroDivisionError('Нельзя делить число на ноль!')
            else:
                return Calculator(self.a / other.a)
        if other == 0:
            raise ZeroDivisionError('Нельзя делить число на ноль!')
        return Calculator(self.a / other)

    def __str__(self):
        return f"Calculator({self.a})"


while True:
    try:
        n1 = Calculator(int(input('Введите число для данного экземпляра: ')))
        break
    except ValueError:
        print('Введите только цифры!')
while True:
    try:
        n2 = Calculator(int(input('Введите число для данного экземпляра: ')))
        break
    except ValueError:
        print('Введите только цифры!')
print(n1 / n2)
