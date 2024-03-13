#Assignment07_Q07

# function that returns the number of vowels
def num_vowels(string):
    # count of vowels
    vowels = 'aeiouAEIOU'
    count = 0
    # Loop over each character in string parameter
    for Char in string:
        # If character is a vowel, increment its count by 1
        if Char in vowels:
            count += 1
    # Return the count of vowels
    return count


# function that returns the number of consonants
def num_consonants(string):
    # count of consonants
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0

    # Loop over each character in string parameter
    for Char in string:
        # If current lowercase character is a consonant, increment its count by 1
        if Char in consonants :
            count += 1

    # Return the count of consonants
    return count


def main():
    # Prompt the user to enter a string
    string = input("Enter a string: ")
    #callback the functions
    vowels = num_vowels(string)
    consonants = num_consonants(string)
    print(f"The string you entered includes {vowels} vowels and {consonants} consonants ")
    

main()

