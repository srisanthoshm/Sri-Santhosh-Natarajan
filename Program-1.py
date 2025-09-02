class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return "Error"
        return self.a / self.b

def format_result(value):
    if isinstance(value, str):
        return value
    if value == int(value):
        return int(value)
    return value
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (add, sub, mul, div): ").lower()
calc = Calculator(a, b)

if op=="add":
    print("Result:", format_result(calc.add()))
elif op=="sub":
    print("Result:", format_result(calc.sub()))
elif op=="mul":
    print("Result:", format_result(calc.mul()))
elif op=="div":
    print("Result:", format_result(calc.div()))
else:
    print("Invalid operation")