#Question 9
import turtle

x1 = float(input("Enter first point x value: "))
y1 = float(input("Enter first point y value: "))
x2 = float(input("Enter second point x value: "))
y2 = float(input("Enter second point y value: "))

# Draw a red line between the two points
turtle.penup()
turtle.goto(x1, y1)
turtle.write(f"({x1:.0f}, {y1:.0f})", align="left", font=("Arial", 12, "normal"))
turtle.color("red")
turtle.pendown()
turtle.goto(x2, y2)
turtle.color("black")
turtle.write(f"({x2:.0f}, {y2:.0f})", align="left", font=("Arial", 12, "normal"))
