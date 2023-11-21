def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operator = input("Enter operator (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Check the operator and perform the corresponding operation
if operator == '1':
    result = add(num1, num2)
elif operator == '2':
    result = subtract(num1, num2)
elif operator == '3':
    result = multiply(num1, num2)
elif operator == '4':
    result = divide(num1, num2)
else:
    result = "Invalid operator"

print(f"Result: {result}")
