#Assignmnet07_Q05

def main():
    # Prompt the use for filename and string to be removed
    filename = input('Enter a filename: ')
    string_remove = input('Enter a string to be removed: ')
    

    # Read the content of the file
    with open(filename, 'r') as file:
        content = file.read()

    # Remove the specified string frm the conent
    updated_content = content.replace(string_remove, '')

    # Write the updaed content back to the file
    with open(filename, 'w') as file:
        file.write(updated_content)
        
        
# Run the main function
if __name__ == "__main__":
    main()
