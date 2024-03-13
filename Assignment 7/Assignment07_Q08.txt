#Assignment07_Q08

#function that takes a string and checks whether a string is a valid password.
def valid_password(password):
    # at least eight characters
    if len(password) < 8:
        return False
    
    # consist of only letters and digits
    if not password.isalnum():
        return False
    
    # contain at least two digits
    digits_count = 0
    for c in password:
        if c.isdigit():
            digits_count += 1
            
    if digits_count < 2:
        return False
    
    # If all rules pass, the password is valid
    return True

def main():
    # Prompt the user to enter a password
    password = input("Enter a password: ")

    # Check if the password is valid 
    if valid_password(password):
        print("Valid password.")
    else:
        print("Invalid password .")


if __name__ == "__main__":
    main()

