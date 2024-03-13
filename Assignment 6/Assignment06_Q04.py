#Assignment06_Q04

def isSorted(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

def main():
    user_input = input("Enter numbers: ").split()
    user_input = [int(x) for x in user_input]
    
    if isSorted(user_input):
        print("The list is already sorted")
    else:
        print("The list is not sorted")

if __name__ == "__main__":
    main()
