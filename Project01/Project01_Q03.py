# Constants
small_cup = 1.75
medium_cup = 1.90
large_cup = 2.00

# Variables to keep track of the coffee shop's sales data
small_cups_sold = 0
medium_cups_sold = 0
large_cups_sold = 0
total = 0

#A)Define a function to print menu 
def menu():
        print("")
        print("1: Enter 1 to order coffee.")
        print("2: Enter 2 to check the total money made up to this time.")
        print("3: Enter 3 to check the total amount of coffee sold up to this time.")
        print("4: Enter 4 to check the number of cups of coffee of each size sold.")
        print("5: Enter 5 to print the data.")
        print("9: Enter 9 to exit the program.")
    


#B)Option 1- Function to order coffee 
def coffee(small_cups_sold, medium_cups_sold, large_cups_sold, total):
    current_order_total = 0
    while True:
        
        print("")
        print("1: Enter 1 to buy coffee in a small cup size (9 oz)")
        print("2: Enter 2 to buy coffee in a medium cup size (12 oz)")
        print("3: Enter 3 to buy coffee in a large cup size (15 oz)")
        print("9: Enter 9 to exit.")
        #prompt the user to chose a size
        size = int(input())

        if size == 1:
            num_cups = int(input("Enter the number of cups: "))
            #update num of small cups sold 
            small_cups_sold += num_cups 
            #update the total cost 
            total += num_cups * small_cup 
            #update the current total cost 
            current_order_total += num_cups*small_cup

        elif size == 2:
            num_cups = int(input("Enter the number of cups: "))
            #update num of medium cups sold 
            medium_cups_sold += num_cups
            total += num_cups * medium_cup
            current_order_total+= num_cups*medium_cup

        elif size == 3:
            num_cups = int(input("Enter the number of cups: "))
            #update num of large cups sold 
            large_cups_sold += num_cups
            total += num_cups * large_cup
            current_order_total += num_cups*large_cup

        elif size == 9:
            print("")
            print(f"Please pay: ${current_order_total:.2f}")
            print("")
            break

    return small_cups_sold, medium_cups_sold, large_cups_sold, total

#C) Option 2 - Function to check the total money 
def check_total_money(total):
    #get total from coffee function
    print(f"Total money made: ${total:.2f}")

#D) Option 3 - Function to check the total amount of coffee sold 
def check_total_coffee_sold(small_cups_sold, medium_cups_sold, large_cups_sold):
    total_coffee_sold = (small_cups_sold * 9) + (medium_cups_sold * 12) + (large_cups_sold * 15)
    print(f"Total amount of coffee sold: {total_coffee_sold} oz")

#E) Option 4 -  Function to check the number of cups of coffee of each size sold 
def check_cup_sizes_sold(small_cups_sold, medium_cups_sold, large_cups_sold):
    print(f"Small cups sold: {small_cups_sold}")
    print(f"Medium cups sold: {medium_cups_sold}")
    print(f"Large cups sold: {large_cups_sold}")

#F) Option 5 -  Function that prints the data 
def print_data(small_cup, medium_cup, large_cup, small_cups_sold, medium_cups_sold, large_cups_sold, total):
    check_cup_sizes_sold(small_cups_sold, medium_cups_sold, large_cups_sold)
    check_total_coffee_sold(small_cups_sold, medium_cups_sold, large_cups_sold)
    check_total_money(total)
    

def main():
    small_cups_sold = 0
    medium_cups_sold = 0
    large_cups_sold = 0
    total = 0
    
    while True:
        menu()
        #prompt the user to choose a option
        option = int(input())

        if option == 1:
            small_cups_sold, medium_cups_sold, large_cups_sold, total = coffee(small_cups_sold, medium_cups_sold, large_cups_sold, total)
        elif option == 2:
            check_total_money(total)
        elif option == 3:
            check_total_coffee_sold(small_cups_sold, medium_cups_sold, large_cups_sold)
        elif option == 4:
            check_cup_sizes_sold(small_cups_sold, medium_cups_sold, large_cups_sold)
        elif option == 5:
            print_data(small_cup, medium_cup, large_cup, small_cups_sold, medium_cups_sold, large_cups_sold, total)
        elif option == 9:
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
