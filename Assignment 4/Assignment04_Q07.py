#Assignment04_Q07
import random

# Define a function that displays the n-by-n matrix
def printMatrix(n):
    for x in range(n):
        for y in range(n):
            print(random.randint(0,1)," ", end="")
        print("\n",end="")

# Define a main function that prompts the user to enter n and prints the matrix
def main():
    n = int(input("Enter a number: "))
    printMatrix(n)

if __name__ == "__main__":
    main()

