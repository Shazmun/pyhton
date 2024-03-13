#Assignment08_Q06

import string

def main():
    # Prompt the user for a file name
    fp = input("Enter the file name: ")
    # Initiize an empty dictionary to store the counts of letter s
    counts = {}

    # Open the file and read its content
    try:
        with open(fp, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File '{fp}' not found.")
        return

    # Iterate through each character in the text
    # heck if the character is a lter and convert it to lowercase
    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            # Update the count in the dictionary
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1

            

    if counts:
        # Print the table header
        print(f"{'Letter':<10}{'Count':<10}")

        # Print the letter and count in a formatted table
        for letter, count in sorted(counts.items()):
            print(f"{letter:<10}{count:<10}")



if __name__ == "__main__":
    main()
