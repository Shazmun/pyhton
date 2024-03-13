#Lab04_part01

weight= float(input("Enter the weight of the package: "))
cost = 0

if weight <= 2:
    cost = 1.10
elif weight <= 6:
    cost = 2.20
elif weight <= 10:
    cost = 3.70
else:
    cost = 3.80

print(f"Shipping charge: ${cost:.2f}")


