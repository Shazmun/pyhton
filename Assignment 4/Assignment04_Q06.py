#Assignment04_Q06
#Define a function that returns the number of days in a year
def numberOfDaysInAYear(year):
     #Check if a year is a leap year and return the number of days in a year.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 366
    else:
        return 365

#Define a main function
def main():
    #Display the number of days in the years from 2000 to 2010."""
    for year in range(2000, 2011):
        num_days = numberOfDaysInAYear(year)
        print(f"{year} has {num_days}")


if __name__ == "__main__":
    main()
