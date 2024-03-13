#Assignment04_Q09
import turtle
import random
# Prompt the user for the width and height of the rectangle
width = float(input("Enter the width of rectangle: "))
height = float(input("Enter the height of rectangle: "))

# Draw a rectangle centered at (0, 0)
turtle.penup()
turtle.goto(-width/2, -height/2)
turtle.pendown()
for _ in range(2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

#Draw a ball at a random position within the rectangle
turtle.penup()
turtle.goto(0, 0)
turtle.pencolor('red')
num_balls = 1
while num_balls <=10:
    x = random.uniform(-width/2, width/2)
    y = random.uniform(-height/2, height/2)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(3)  # Assuming the radius of the ball is 
    turtle.end_fill()
    turtle.penup()
    num_balls += 1

turtle.hideturtle()
