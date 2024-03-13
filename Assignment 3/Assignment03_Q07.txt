#Assignment03_Q07

import math
# Initialize the total sum to 0 and the starting value of num to 1
total = 0  
num = 1  
# Loop while num is less than or equal to 624
while num <= 624:
    # Calculate the sum by adding the current term to the total
    total += 1 / (math.sqrt(num) + math.sqrt(num + 1))
    num += 1  # Increment num by 1 for the next iteration

print(f"The sum is {total:.3f}")
