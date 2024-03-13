#Lab02
#milk carton can hold 3.78 liters of milk
milk_capacity = 3.78
#cost of producing one liter of milk is $0.38
milk_cost_per_liter = 0.38
#the profit of each carton of milk is $0.27
profit_of_each_carton = 0.27

milk_quantity = float(input("Enter, in liters, the total quantity of milk produced: "))

number = int(milk_quantity/milk_capacity)
cost = milk_quantity*milk_cost_per_liter
profit =  number*profit_of_each_carton

print("The number of milk cartons needed to hold milk: ", number)
print("The cost of producing milk: {:.2f}".format(cost))
print("Profit: {:.2f}".format(profit))
