#Lab04_part02

rate = float(input("Enter the exchange rate from U.S. dollars to Canadian dollars: "))
convert = int(input("Enter 0 to convert U.S. dollars to Canadian dollars and 1 vice versa: "))

if convert == 0:
    USD_amount = float(input("Enter the U.S. dollar amount: "))
    CAD_amount = USD_amount * rate
    print(f"{USD_amount:.2f} U.S. dollars is {CAD_amount:.2f} Canadian dollars")
elif convert== 1:
    CAD_amount = float(input("Enter the Canadian dollars amount: "))
    USD_amount = CAD_amount /rate
    print(f"{CAD_amount:.2f} Canadian dollars is {USD_amount:.2f} U.S. dollars")
else:
    print("Invalid Conversion Type")


















