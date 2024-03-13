
#part 02: compute the state and county sales tax
purchase_amount = float(input("Enter the amount of the purchase: "))
state_tax = purchase_amount * 0.04
county_tax = purchase_amount * 0.02
total_tax = state_tax + county_tax
sale_total = purchase_amount + total_tax
print("Purchase Amount: {:.2f}".format( purchase_amount ))
print("State Tax: {:.2f}".format(state_tax))
print("County Tax: {:.3f}".format(county_tax))
print("Total Tax: {} " .format(total_tax))
print("Sale total: {:.3f}" .format(sale_total))
