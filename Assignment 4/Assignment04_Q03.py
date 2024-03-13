#Assignment04_Q03

# Define a function named 'maximum' that takes two integer arguments and returns the greater of the two.
def maximum(num1, num2):
    return max(num1, num2)

# Define a function named 'main' to handle user input and display the maximum number.
def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
# Call the 'maximum' function to find the maximum of the two numbers.
    max_number = maximum(num1, num2)
    print("The maximum number is:", max_number)

if __name__ == "__main__":
    main()

