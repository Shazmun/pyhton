#Assignment03_Q9

import turtle
# Set the starting position to (0, 0)
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()

r = 50 # Set the initial radius

for i in range(10): # Iterate 10 times
    # Set the color based on whether i is even or odd
    if i % 2 == 0:
        turtle.color('red')
    else:
        turtle.color('blue')
    turtle.circle(r) # Draw a circle with the current radius
    r += 10  # Increase the radius for the next iteration

    # Move to the next position
    turtle.penup()
    turtle.goto(0, -r)
    turtle.pendown()

# Hide the turtle
turtle.hideturtle()








