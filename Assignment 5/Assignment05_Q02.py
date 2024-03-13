#Assigment05_Q02

# Define a function to check if a given integer is prime
def is_prime(integer):
    # Check if the integer is less than or equal to 1, it's not prime
    if integer <= 1:
        return False
    # Check if the integer is 2 or 3, it's prime
    if integer <= 3:
        return True

    # Check if the integer is divisible by 2 or 3, it's not prime
    if integer % 2 == 0 or integer % 3 == 0:
        return False

    # Initialize a divisor candidate at 5
    i = 5
    # Iterate until the square of the candidate is less than or equal to the integer
    while i * i <= integer:
        # Check if the integer is divisible by i or (i + 2), where i + 2 is also a potential divisor
        if integer % i == 0 or integer % (i + 2) == 0:
            return False
        # Increment the candidate by 6 for optimization
        i += 6

    # If none of the conditions above are met, the integer is prime
    return True

# Define a main function to take user input, call the is_prime function, and display the result
def main():
    integer = int(input("Enter an integer: ")) 
    prime = is_prime(integer) 
    if prime:
        print("The number you entered is a prime number.")
    else:
        print("The number you entered is not a prime number.")


if __name__ == "__main__":
    main()
