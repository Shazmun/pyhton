#Assignment06_Q05

def sort_tuple(numbers_tuple):
    sorted_tuple = tuple(sorted(numbers_tuple))
    return sorted_tuple

def main():
    numbers = input("Enter 10 integers on the same line: ")
    numbers = [int(x) for x in numbers.split()]
    
    if len(numbers) != 10:
        print("Please enter exactly 10 integers.")
        return

    numbers_tuple = tuple(numbers)
    print("Before sorting", numbers_tuple)
    sorted_tuple = sort_tuple(numbers_tuple)
    print("After sorting", sorted_tuple)

if __name__ == "__main__":
    main()
