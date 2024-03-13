#Assignment04_Q08
import random

for i in range(5):
    # Generate a random three-digit number with all digits the same
    lottery_number = random.randint(1, 9) * 111
    print(f'Lottery number{i + 1}: {lottery_number}')

