#Assignmnet07_Q04

import csv

def main():
    # Read data from the CSV file
    with open("products.csv", 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    # Display header with proper formatting
    header = data[0]
    print(f"{header[0]:<8} {header[1]:<8} {header[2]:<8}")
    #initialize
    total_suits_price = 0
    total_shoes_price = 0
    
    # Iterate through the data (starting from index 1 to skip the header)
    for row in data[1:]:
        if len(row) >= 3:  # Check if the row has at least 3 elements
            print(f"{row[0]:<8} {row[1]:<8} {row[2]:<8}")
            if row[0] == 'suit':
                total_suits_price += int(row[2])
            elif row[0] == 'shoes':
                total_shoes_price += int(row[2])
        
        
    print()
    print(f"Total suits price {total_suits_price}")
    print(f"Total shoes price {total_shoes_price}")

if __name__ == "__main__":
    main()