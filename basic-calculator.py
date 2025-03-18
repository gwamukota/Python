# Simple Calculator Program for Beginners

# Enter the first number
num1 = input("Enter the first number: ")

# Enter the second number
num2 = input("Enter the second number: ")

# Choose a mathematical operation: +, -, *, or /
operation = input("Enter the operation (+, -, *, /): ")

# Convert the string inputs to float numbers to perform calculations
num1 = float(num1)
num2 = float(num2)

# Perform the calculation based on the chosen operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Check for division by zero
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        exit()  # Exit the program if division by zero
    result = num1 / num2
else:
    print("Invalid operation!")
    exit()  # Exit the program if the operation is not recognized

# Print the result in the format: num1 operation num2 = result
print(f"{num1} {operation} {num2} = {result}")
