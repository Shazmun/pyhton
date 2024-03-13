#Assignment04_Q02

num_years= int(input("Enter the number of years: "))
total_rainfall= 0
total_months = num_years*12

# Outer loop for each year
for years in range (1, num_years +1):
    print(f"For year {years}:")
# Inner loop for each month
    for month in range ( 1,13):
        rainfall_amount= float (input(f"Enter the reinfall amount for the month {month}: " ))
        total_rainfall += rainfall_amount
    # Calculate average rainfall per month
    average_rainfall = total_rainfall / total_months
    

print(f"For {total_months} months")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")


            
                                
