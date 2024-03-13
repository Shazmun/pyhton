#Assignment06_Q01

def num(integers):
    for num in set(integers):  
        count = integers.count(num)
        print(f"{num} occurs {count} times")

def main():
    integers = input("Enter the integers between 1 and 100: ")
    integers = list(map(int, integers.split()))
    
    # Check if all integers are between 1 and 100
    if all(1 <= num <= 100 for num in integers):  
        num(integers)
    else:
        print("Please enter integers between 1 and 100.")

if __name__ == "__main__":
    main()
