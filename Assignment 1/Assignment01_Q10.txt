#Question 10
import turtle

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
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()

# Draw the rectangle
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.hideturtle()
