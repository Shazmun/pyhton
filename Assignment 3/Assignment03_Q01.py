# Assignment03_Q01

# Initialize the variables
total = 0
positives = 0
negatives = 0

while True: # Infinite loop until a break condition is met
    integer = int(input("Enter an integer, the input ends if it is 0: "))
    if integer == 0: # Exit the loop if the input is 0
        break
    total += integer  # Accumulate the total sum of non-zero integers
    # Count the number of positive and negative integers
    if integer > 0:
        positives += 1
    elif integer < 0:
        negatives += 1

if total != 0:
     # Calculate the average of the non-zero numbers and print the result
    average = total / (positives + negatives)
    print(f"The number of positives is {positives}")
    print(f"The number of negatives is {negatives}")
    print(f"The total is {total}")
    print(f"The average is {average:.2f}")
else:
   print("No numbers are entered except 0")
