#Project02_Q02

import string

# A - Function to write data from a list to a file
def file(data_list, output_file):
    with open(output_file, 'w') as file:
        for item in data_list:
            file.write(item + '\n')

# B - Function that creates a list of unique words from a file 
def uniqueword(filename):
    with open(filename, 'r') as file:
        words = file.read().lower().split()
        punctuations = "!()-[]{};:\'\",./?@#$%^&*~"
        no_punctuations= ""
        # Remove punctuation from each word
        for word in words:
            for char in word:
                if char not in punctuations:
                    no_punctuations= no_punctuations+ char
            no_punctuations = no_punctuations + ","

        no_punctuations = no_punctuations.split(",")
        
        unique_words = []
        final_words = "" #only for printing
        for word in no_punctuations:
            if word not in unique_words:
                unique_words.append(word)
        # Remove the last empty string from the list
        unique_words.pop()
        # Combine unique words into a string
        for word in unique_words:
            final_words = final_words + word + " "
        return final_words

# C - Function that creates a list of union words
def unionword(file1, file2):
    words_file1 = uniqueword(file1)
    words_file2 = uniqueword(file2)
    union_words = ""
    # Combine unique words from both files
    for word in words_file1.split():
        union_words += word + " "

    for word in words_file2.split():
        if word not in union_words:
            union_words += word + " "

    return union_words.strip()


# D - Function that creates a list of common words
def commonword(file1, file2):
    words_file1 = uniqueword(file1)
    words_file2 = uniqueword(file2)
    
    commonwords = ""
    # Find common words between both files
    for word in words_file1.split():
        if word in words_file2:
            commonwords += word + " "

    return commonwords.strip()

# E - Function that creates a list of words in one file but not in another file 
def differenceword(file1, file2):
    words_file1 = uniqueword(file1).split()
    words_file2 = uniqueword(file2).split()
    # Find words in file1 but not in file2
    diff_file1_file2 = []
    for word in words_file1:
        if word not in words_file2:
            diff_file1_file2.append(word)
    # Find words in file2 but not in file1
    diff_file2_file1 = []
    for word in words_file2:
        if word not in words_file1:
            diff_file2_file1.append(word)

    return diff_file1_file2, diff_file2_file1

# F- Function to print the count of each word in a file
def word_count(words):
        word_count = {}
        #count the words
        for word in words:
            word_count.setdefault(word, 0)

        for word in words:
            word_count[word] += 1

        result = f"Word{'':<60}Count\n"
        for word, count in word_count.items():
            result += f"{word:<60}{count}\n"
        return result
# H - Function to read data from a file
def read_file_words(filename):
    with open(filename, 'r') as file:
        words = file.read().lower().split()
        words = [word.strip(string.punctuation) for word in words]
        return words

# Now you can use this function in your main function or elsewhere in your script.
# G - Main function
def main():
    file1 = input("Enter the name of the first input file: ")
    file2 = input("Enter the name of the second input file: ")
    output_file = 'fileAnalysis.txt'
    
    # Call the functions to get the results
    words_file1 = read_file_words(file1)
    words_file2 = read_file_words(file2)
    unique_words_file1 = uniqueword(file1)
    unique_words_file2 = uniqueword(file2)
    union_words = unionword(file1, file2)
    common_words = commonword(file1, file2)
    diff_file1_file2, diff_file2_file1 = differenceword(file1, file2)
    word_file1 = word_count(words_file1)
    word_file2 = word_count(words_file2)

    output_data = [
        f"Unique words in file 1: {unique_words_file1}",
        f"Unique words in file 2: {unique_words_file2}",
        f"Union of words in file 1 and file 2: {union_words}",
        f"Intersection of words in file 1 and file 2: {common_words}",
        f"Words in file 1 but not in file 2: {' '.join(diff_file1_file2)}",
        f"Words in file 2 but not in file 1: {' '.join(diff_file2_file1)}",
        f"Words in file 1 but not in file 2 and words in file 2 but not in file 1: {' '.join(diff_file1_file2 + diff_file2_file1)}",
        f"Word Frequency in file 1:\n{word_file1}",
        f"Word Frequency in file 2:\n{word_file2}",
    ]

   # Write results in the output file
    file(output_data, output_file)
    
    print(f"Data saved in {output_file}")

if __name__ == "__main__":
    main()


