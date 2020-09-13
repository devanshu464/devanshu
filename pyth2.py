#simple calculator operational on only two values
class Calculator:
    def __init__(self):
        self.x = 10
        self.y = 20

    def add(self, a, b):
        c = a +b
        return c
    def sub(self, a, b):
        c = a - b
        return c

    def mul(self, a, b):
        c = a*b
        return c
    def pow(self, a, b):
        c = a ** b
        return c
    def div(self, a, b):
        c = a / b
        return c

c1 = Calculator()
print(c1.add(10,20))
print(c1.sub(10,20))
print(c1.mul(10,20))
print(c1.pow(10,20))
print(c1.div(10,20))
