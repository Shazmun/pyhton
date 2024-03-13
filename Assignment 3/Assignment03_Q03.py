# Assignment03_Q03

# Define units for kilograms and pounds
kg = "Kilograms"
lb = "Pounds"

# Print headers for the table
print(f"{kg:<12}{lb:<12}\t|\t\t{lb:<12}{kg:<12}")

# Loop through numbers from 0 to 99
for num in range(0, 100):
    # Calculate kilogram iteration based on the loop variable
    kilo_iter = num * 2 + 1

    # Calculate pound iteration based on the loop variable
    pound_iter = num * 5 + 20

    # Convert kilogram iteration to pounds
    lb = kilo_iter * 2.2

    # Convert pound iteration to kilograms
    kg = pound_iter * 0.4545

    # Print the values in a formatted table
    print(f"{kilo_iter:<12}{lb:<12.1f}\t|\t\t{pound_iter:<12}{kg:<12.2f}")
