#Assignment06_Q03

def eliminateDuplicates(lst):
    new_lst = []
    for num in lst:
        if num not in new_lst:
            new_lst.append(num)
    return new_lst


def main():
    input_numbers = input("Enter numbers: ")
    numbers = input_numbers.split()
    numbers = [int(num) for num in numbers]

    distinct_numbers = eliminateDuplicates(numbers)
    print("The distinct numbers are:", distinct_numbers)
main()