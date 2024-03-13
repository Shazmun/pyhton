#Assignment04_Q01

# Outer loop to iterate from 1 to 10 (inclusive)
for num in range(1, 11):
    # Inner loop to print numbers from 1 to the current row number (inclusive)
    for j in range(1, num + 1):
        # Print the current number followed by a space
        print(j, end=" ")
    # Move to the next line after printing the numbers for the current row
    print()

    
