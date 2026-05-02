class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


# Create object
calc = Calculator()

# User Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", calc.add(num1, num2))
elif choice == '2':
    print("Result:", calc.subtract(num1, num2))
elif choice == '3':
    print("Result:", calc.multiply(num1, num2))
elif choice == '4':
    print("Result:", calc.divide(num1, num2))
else:
    print("Invalid Choice")
    