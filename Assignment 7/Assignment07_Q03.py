#Assignment07_Q03


def main():

    with open('BoyNames.txt') as boy_file:
            boy_names = [line.strip() for line in boy_file]

    with open('GirlNames.txt') as girl_file:
        girl_names = [line.strip() for line in girl_file]

    # Get user input for boy's name and girl's name 
    boy_name = input("Enter a boy's name, or N if you do not wish to enter a boy's name: ")
    girl_name = input("Enter a girl's name, or N if you do not wish to enter a girl's name: ")
    
    if boy_name == 'N':
        print("You chose not to enter a boy's name")
    else:
        boy_name = boy_name.strip()
        if boy_name in boy_names:
            print(f"{boy_name} is one of the most popular boy's names")
        else:
            print(f"{boy_name} is not one of the most popular boy's names")

    
    if girl_name == 'N':
        print("You chose not to enter a girl's name")
    else:
        girl_name = girl_name.strip()
        if girl_name in girl_names:
            print(f"{girl_name} is one of the most popular girl's names")
        else:
            print(f"{girl_name} is not one of the most popular girl's names")

if __name__ == "__main__":
    main()
