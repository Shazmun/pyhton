#Question 07
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
operator = input("Enter operator (+ - * /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "ERROR: Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Illegal operation"

print(f"{num1} {operator} {num2} = {result}")
