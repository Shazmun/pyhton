#Lab12

def relatives(data, familyName):
    l= []
    for first, last in data.items():
        if last == familyName:
            l.append(first)
    return l

def main():
    data = {}
    print("Enter 6 names:")
    for i in range(6):
        first, last = input().split()
        data[first.strip()] = last.strip()
    print()

    familyName = input("Enter family name: ")
    print()

    f = "First Name"
    l = "Last Name"
    print(f"{f:<15s}{l:<15s}")
    for first, last in data.items():
        print(f"{first:<15s}{last:<15s}")
    print()

    L = relatives(data, familyName)

    if len(L) >= 2:
        print(f"Persons with the same last name {familyName}: ")
        for relative in L:
            print(relative)
    else:
        print(f"No persons with the same last name.")

if __name__ == "__main__":
    main()
