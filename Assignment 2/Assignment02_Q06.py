import turtle

# Input for p0
x0 = int(input("Enter the x coordinate of p0: "))
y0 = int(input("Enter the y coordinate of p0: "))
p0 = (x0, y0)

# Input for p1
x1 = int(input("Enter the x coordinate of p1: "))
y1 = int(input("Enter the y coordinate of p1: "))
p1 = (x1, y1)

# Input for p2
x2 = int(input("Enter the x coordinate of p2: "))
y2 = int(input("Enter the y coordinate of p2: "))
p2 = (x2, y2)

# Draw line between p0 and p1
turtle.penup()
turtle.goto(p0)
turtle.write(f' p1{p0}', font=("Arial", 12, "normal"))
turtle.pendown()
turtle.goto(p1)
turtle.write(f' p2{p1}',  font=("Arial", 12, "normal"))

# Draw point p2
turtle.penup()
turtle.goto(p2)
turtle.dot(6)  # Display p2 as a dot

# Determine and display the relation of p2 to the line
distance = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
if distance  > 0:
    turtle.write("p2 is on the left side of the line",font=("Arial", 12, "normal"))
elif distance  < 0:
    turtle.write("p2 is on the right side of the line", font=("Arial", 12, "normal"))
else:
    turtle.write("p2 is on the same line",  font=("Arial", 12, "normal"))

turtle.hideturtle()

