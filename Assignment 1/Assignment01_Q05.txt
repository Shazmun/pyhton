#Question 5

temp = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))
speed = float(input("Enter the wind speed miles per hour (must be greater than or equal to 2): "))
wind_chill = 35.74 + 0.6215 * temp - 35.75 * speed**0.16 + 0.4275* temp * speed**0.16
print("The wind chill index is {:.2f}".format(wind_chill))

