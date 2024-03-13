#Question 1
a = ((9.5*4.5)-(2.5*3))/(45.5-3.5)
print(float(a))

#Question 2
pi= 4*(1-1/3+1/5-1/7+1/9-1/11)
pi_2= 4*(1-1/3+1/5-1/7+1/9-1/11+1/13-1/15)
print(pi)
print(pi_2)


#Question 3
current_population = 312032486
seconds_per_year = 365*24*60*60

births = 1/7 * seconds_per_year
deaths = 1/13 * seconds_per_year
immigrants = 1/45 * seconds_per_year

updated_population = births - deaths + immigrants

one_year = current_population + updated_population
two_year = one_year + updated_population
three_year = two_year + updated_population
four_year = three_year + updated_population
five_year = four_year + updated_population

print("population after one year: {:.0f}".format(one_year))# this is not right work on it 
print("population after two years: {:.0f}".format(two_year))
print("population after three years:{:.0f} ".format(three_year))
print("population after four years: {:.0f}".format(four_year))
print("population after five years: {:.0f}".format(five_year))


#Questions 4
user_input  = float(input("Enter a value for feet:"))
feet = 0.305
meters = feet* user_input 
print("{:.1f} feet is {:.4f} meters".format(user_input , meters))

#Question 5
temp = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))
speed = float(input("Enter the wind speed miles per hour (must be greater than or equal to 2): "))
wind_chill = 35.74 + 0.6215 * temp - 35.75 * speed**0.16 + 0.4275* temp * speed**0.16
print("The wind chill index is {:.2f}".format(wind_chill))

#Queastion 6

#import math

# Print the table header
#print(f'a{" " * 9}b{" " * 9}pow(a, b)')
#print('-' * 30)

# Define a list of values for 'a'
#a_values = [1, 2, 3, 4, 5]

# Calculate 'b' as 'a + 1' for each 'a' value
#b_values = [a + 1 for a in a_values]

# Calculate 'pow(a, b)' for each pair of 'a' and 'b' values
#result_values = [math.pow(a, b) for a, b in zip(a_values, b_values)]

# Print the rows with formatting using a zip function
#for a, b, result in zip(a_values, b_values, result_values):
    #print(f'{a:<10}{b:<10}{result:.1f}')



#Question 6








#Queston 7

integer = int(input("Enter a four-digit integer: " ))

interger_4 = integer % 10
integer //= 10
interger_3 =integer % 10
integer //= 10
interger_2 = integer % 10
integer //= 10
interger_1 = integer % 10


print(interger_4)
print(interger_3)
print(interger_2)
print(interger_1)


#Question 8
import math
side = float(input("Enter the side: " ))
area = (3*math.sqrt(3)/2)*(side**2)
print("The area of the hexagon is {:.3f}".format(area))

#Question 9
import turtle
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(1)  


x1 = float(input("Enter first point x value: "))
y1 = float(input("Enter first point y value: "))
x2 = float(input("Enter second point x value: "))
y2 = float(input("Enter second point y value: "))

# Draw a red line between the two points
pen.penup()
pen.goto(x1, y1)
pen.write(f"({x1:.0f}, {y1:.0f})", align="left", font=("Arial", 12, "normal"))
pen.color("red")
pen.pendown()
pen.goto(x2, y2)
pen.color("black")
pen.write(f"({x2:.0f}, {y2:.0f})", align="left", font=("Arial", 12, "normal"))


#Question 10
import turtle

# Set up the screen and pen
screen = turtle.Screen()
pen = turtle.Turtle()
pen.speed(1)

# Prompt the user for input
x = float(input("Enter x coordinate for the center of the rectangle: "))
y = float(input("Enter y coordinate for the center of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

# Calculate the coordinates of the corners of the rectangle
x1 = x - width / 2
x2 = x + width / 2
y1 = y - height / 2
y2 = y + height / 2

# Move the pen to the starting point
pen.penup()
pen.goto(x1, y1)
pen.pendown()

# Draw the rectangle
pen.forward(width)
pen.left(90)
pen.forward(height)
pen.left(90)
pen.forward(width)
pen.left(90)
pen.forward(height)
pen.hideturtle()
















