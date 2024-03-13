#Question 3

integer= int(input("Enter an integer: "))

if integer % 5 == 0 and integer % 6 == 0 :
    print(f"{integer} is divisible by both 5 and 6")
elif integer % 5 == 0 or integer % 6 == 0 :
    print(f"{integer} is divisible by both 5 and 6, but not both")
else:
    print(f"{integer} not divisible by either 5 or 6")
