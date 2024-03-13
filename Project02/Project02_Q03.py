#Project02_Q03
import json

#A) Function to display a menu 
def display_menu():
    print("Menu")
    print("----------------------------------------")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")

#B) Option 1 - A function to look up a person’s email address
def lookup(d):
    name = input("Enter the name to look up: ")
    email = d.get(name)
    if email:
        print(f"Name: {name}")
        print(f"Email:{email}")
    else:
        print(f"The specified name was not found")
    
    return
    
#c) Option 2 - A function to add a new name and email address
def add(d):
    name = input("Enter the name: ")
    email = input("Enter the email address: ")
    
    # Check if the name already exists
    if name in d:
        print("That name already exists.")
    else:
        d[name] = email
        print("Name and address have been added.")
      

#D) Option 3 - Afunction to change an email address
def change(d):
    name = input("Enter name: ")
    if name in d:
        new_email = input("Enter the new address: ")
        d[name] = new_email
        print(f"Information updated")
    else:
        print("The specified name was not found")

#E) Option 4 - A function to delete a name and email address.
def delete(d):
    name = input("Enter name: ")
    if name in d:
        del d[name]
        print(f"Information deleted")
    else:
        print("The specified name was not found.")


def main():

    with open("contacts.json", "r") as file:
        data = json.load(file)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            lookup(data)
        elif choice == "2":
            add(data)
        elif choice == "3":
            change(data)
        elif choice == "4":
            delete(data)
        elif choice == "5":
            # Save data before exiting
            with open("contacts.json", "w") as file:
                json.dump(data, file)
            print("Information Saved")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()