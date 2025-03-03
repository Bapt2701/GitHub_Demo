# Simple Calculator

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user input for operation choice
choice = input("Enter your choice (1/2/3/4): ")

# Take user input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the chosen operation
if choice == '1':
    result = add(num1, num2)
    operator = '+'
elif choice == '2':
    result = subtract(num1, num2)
    operator = '-'
elif choice ==
