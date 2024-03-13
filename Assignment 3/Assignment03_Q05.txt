#Assignment03_Q05

# Prompt the user to enter loan amount and number of years
loan_amount = float(input("Enter loan amount, for example 120000.95: "))
num_years = int(input("Enter the number of years as an integer, for example 5: "))
interest_rate = 5.0

# skip to newline
print("\n")

# Print the heading
print("Interest Rate\tMonthly Payment\tTotal Payment")

# Loop through interest rates from 5.0% to 8.0%
while interest_rate <= 8.0:
    # Calculate the monthly interest rate
    monthly_interest_rate = interest_rate / 1200
    
    # Calculate the monthly payment using the loan formula
    monthly_payment = loan_amount * monthly_interest_rate / (1 - 1 / (1 + monthly_interest_rate) ** (num_years * 12))
    
    # Calculate the total payments over the loan term
    total_payments = monthly_payment * num_years * 12
    
    # Print the interest rate, monthly payment, and total payment in a formatted manner
    print(f"{interest_rate:.3f}%\t\t\t{monthly_payment:.2f}\t\t\t{total_payments:.2f}")
    
    # Increment the interest rate by 1/8 for the next iteration
    interest_rate += (1 / 8)
