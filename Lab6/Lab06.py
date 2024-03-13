import random

while True:
    print("Enter 1 to generate a random number between 1 and 100 ")
    print("Enter 2 to generate a random even number between 1 and 100 ")
    print("Enter 3 to generate 10 random numbers between 1 and 100 ")
    print("Enter 4 to generate 5 random odd numbers between 1 and 100 and print them with their sum ")
    print("Enter 5 to exit")
    
    choice = int(input())

    if choice == 1:
        print("Random number between 1 and 100:", random.randint(1, 100))

    elif choice == 2:
        random_even = random.randint(1, 100)
        while random_even % 2 != 0:
            random_even = random.randint(1, 100)
        print("Random even number between 1 and 100:", random_even)

    elif choice == 3:
        print("10 random numbers:", end=" ")
        for _ in range(10):
            print(random.randint(1, 100), end=" ")
        print()

    elif choice == 4:
        print("Random odd numbers and their sum: ", end=" ")
        s = 0
        for i in range(5):
            x= random.randint(1, 100)
            while  x % 2 !=1:
                x=  random.randint(1, 100)
            print(x, end= " ")
            s = s+x
        print("sum = ", s)
    elif choice == 5:
        break

