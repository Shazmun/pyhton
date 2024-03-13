#Assignment06_Q02

import random

def shuffle(lst):
    n = len(lst)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

def main():
    numbers= input("Enter numbers: ")
    numbers = list(map(int, numbers.split()))
    shuffle(numbers)
    print(numbers)

if __name__ == "__main__":
    main()
