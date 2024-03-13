#Assignment08_Q03

def main():
    # Create a dictionary mapping digits to words
    num = { "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine" }

    # Prompt the user for an integer
    integer = input("Enter an integer to convert to words: ")

    # Convert the integer to a string and loop through each character
    for ch in str(integer):
        # Print the word for the digit
        print(num[ch], end=" ")

if __name__ == "__main__":
    main()
