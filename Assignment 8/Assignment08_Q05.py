#Assignment08_Q05

# Function to get the interction of characters between two strings
def get_intersection(fn, ln):
    return set(fn) & set(ln)

# Function to get the union of characters from two strings
def get_union(fn, ln):
    return set(fn) | set(ln)

# Function to get the symmric difference of characters between two strings
def get_symmetric_difference(fn, ln):
    return set(fn) ^ set(ln)

# Main function to take user input and denstrate the functions
def main():
    # Take user input for first and last names
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    # Call functions to get interseon, union, and symmic difference
    intersection_check = get_intersection(first_name, last_name)
    union_check = get_union(first_name, last_name)
    symmetric_check = get_symmetric_difference(first_name, last_name)

    # Display the relts
    print(f"Intersection: {intersection_check}")
    print(f"Union: {union_check}")
    print(f"Symmetric: {symmetric_check}")

if __name__ == "__main__":
    main()
