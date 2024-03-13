#Assignment03_Q06

# Initialize a counter to keep track of leap years
count = 0

# Loop through the years in the range
for year in range(2001, 2100):
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Print the leap year followed by a space
        print(year, end=" ")
        count += 1

        # Start a new line after every ten leap years
        if count == 10:
            print()  # Start a new line
            count = 0  # Reset the leap year count
