def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    else:
        print("Invalid operation. Please enter '+', '-'or '*': ")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Choose an operation (+, - or *): ")

result = calculator(a, b, operation)

print(f"The result is: {result}")
