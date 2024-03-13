#Assignmnet07_Q06


import random

def random_strings(length):
    random_str = ""
    for i in range(length):
        random_ascii = random.randint(97, 122)
        random_str += chr(random_ascii)
    return random_str


def main():
    # Get user input for the length of the string
    length = int(input("Enter length of a string: "))
    
    random_str = random_strings(length)
    print(f"The random string is: {random_str}")


if __name__ == "__main__":
    main()
