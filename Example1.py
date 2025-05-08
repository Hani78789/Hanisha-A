#simple claculator create using js class
 class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'divide':
            return self.a / self.b if self.b != 0 else "Division by zero error"
        else:
            return "Invalid operation"

# Example usage
cal = Calculator(10, 39, "Add")
print(cal.calculate())
#output 49