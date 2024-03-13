#Assignment06_Q08

import matplotlib.pyplot as plt

def main():
    categories = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
    expenses = []

    print("Enter the expenses for last month in the following categories:")
    
    for category in categories:
        expense = int(input(f'{category}: '))
        expenses.append(expense)

    # Create a pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(expenses, labels=categories,  startangle=140)
    plt.title('Monthly Expenses')
    plt.show()

if __name__ == "__main__":
    main()
