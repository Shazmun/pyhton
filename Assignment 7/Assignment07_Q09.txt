#Assignment07_Q09
#function that checks whether two words are anagrams
def isAnagram(string_1, string_2):
    # convert to lowercase for case-insensitive comparison
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    
    # Convert strings to lists and sort them
    string_1_list = sorted(list(string_1))
    string_2_list = sorted(list(string_2))

    # Compare the sorted lists
    if string_1_list == string_2_list:
        return True
    else:
        return False

def main():
    # Prompt user to enter two strings
    string_1 = input("Enter the first string: ")
    string_2 = input("Enter the second string: ")

    # Check if the entered strings are anagrams
    if isAnagram(string_1, string_2):
        print(f'{string_1} and {string_2} are anagrams.')
    else:
        print(f'{string_1} and {string_2} are not anagrams.')


if __name__ == "__main__":
    main()
