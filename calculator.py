def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y
#mali told to add comments to the code
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operation (+, -, *, /): ")

if c == "+":
    print("Result:", add_numbers(a, b))
elif c == "-":
    print("Result:", subtract_numbers(a, b))
elif c == "*":
    print("Result:", multiply_numbers(a, b))
elif c == "/":
    print("Result:", divide_numbers(a, b))
else:
    print("Invalid input.")