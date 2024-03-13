#Project01_Q01
# A) Function to print out purpose and option
def menu():
    print("This pogram performs operations on fraction. Enter")
    print("1. To add fraction")
    print("2. To subtract fraction ")
    print("3. To multiply fraction ")
    print("4. To divide fraction ")
    print("9.To exit the program")
    option = int(input())
    return option 
# B) Option 1 - Function to add fraction
def addFractions(n1, d1, n2, d2):
    # Perform the fraction adding
    numerator = (n1 * d2) + (n2 * d1)
    denominator = d1 * d2
    return (numerator, denominator)

# c) Option 2 - Function to subtract fraction
def subtractFractions(n1, d1, n2, d2):
    # Perform the fraction subtracting
    numerator = (n1 * d2) - (n2 * d1)
    denominator = d1 * d2
    return (numerator, denominator)

# D) Option 3 - Function to multiply fraction
def multiplyFractions(n1, d1, n2, d2):
    # Perform the fraction multiplying
    numerator = n1 * n2
    denominator = d1 * d2
    return (numerator, denominator)

# E) Option 4 - Function to divide fraction
def divideFractions(n1, d1, n2, d2):
    # Perform the fraction division
    numerator = n1 * d2
    denominator = d1 * n2
    return (numerator, denominator)


#main function that calls all other functions and allows the user to select from

def main():
    while True: 
        # Get the user's choice from the menu
        option = menu()
        
        if option == 1:
            # Addition of fractions
            print("For fraction 1")
            n1 = int(input("Enter the numaretaor: "))
            d1 = int(input("Enter the denomiaetor:"))
            print("For fraction 2")
            n2 = int(input("Enter the numaretaor: "))
            d2 = int(input("Enter the denomiaetor:"))
            # Call the addFractions function
            result = addFractions(n1, d1, n2, d2)
            print(f"{n1}/{d1} + {n2}/{d2} = {result[0]}/{result[1]}")
            print()
            
        elif option == 2:
            # subtracting of fractions
            print("For fraction 1")
            n1 = int(input("Enter the numaretaor: "))
            d1 = int(input("Enter the denomiaetor:"))
            print("For fraction 2")
            n2 = int(input("Enter the numaretaor: "))
            d2 = int(input("Enter the denomiaetor:"))
            # Call the subtractFractions function
            result= subtractFractions(n1, d1, n2, d2)
            print(f"{n1}/{d1} + {n2}/{d2} = {result[0]}/{result[1]}")
            print()
            
        elif option == 3:
            # multiplication of fractions
            print("For fraction 1")
            n1 = int(input("Enter the numaretaor: "))
            d1 = int(input("Enter the denomiaetor: "))
            print("For fraction 2")
            n2 = int(input("Enter the numaretaor: "))
            d2 = int(input("Enter the denomiaetor: "))
            # Call the multipleFractions function
            result= multiplyFractions(n1, d1, n2, d2)
            print(f"{n1}/{d1} + {n2}/{d2} = {result[0]}/{result[1]}")
            print()
            
        elif option == 4:
            # division of fractions
            print("For fraction 1")
            n1 = int(input("Enter the numerator: "))
            d1 = int(input("Enter the denominator: "))
            # MAke sure that the denominators are nonzero
            while d1 == 0:
                print("The denominator must be nonzero.")
                d1 = int(input("Enter the denominator: "))
            print("For fraction 2")
            n2 = int(input("Enter the numerator: "))
            # MAke sure that the numerators are nonzero
            while n2 == 0:
                print("To divide, the second fraction must be nonzero.")
                n2 = int(input("Enter a nonzero number for the numerator: "))
            d2 = int(input("Enter the denominator: "))
            # MAke sure that the denominators are nonzero
            while d2 == 0:
                print("The denominator must be nonzero.")
                d2 = int(input("Enter the denominator: "))
            # Call the divideFractions function
            result = divideFractions(n1, d1, n2, d2)
            print(f"{n1}/{d1} / {n2}/{d2} = {result[0]}/{result[1]}")
        
        elif option == 9:
            break

    

if __name__ == "__main__":
    main()

