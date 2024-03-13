#Assignment05_Q06
import turtle

# Fill a rectangle with the specified color, center, width, and height.
def drawRectangle(color = "black", x = 0, y = 0, width = 30, height = 30):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x - width / 2, y - height / 2)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Fill a circle with the specified color, center, and radius.
def drawCircle(color = "black", x = 0, y = 0, radius = 50):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
def main():
    rectangle_color = input("Enter color of the rectangle: ")
    x_center= int(input("Enter x center of the rectangle: "))
    y_center= int(input("Enter y center of the rectangle: "))
    width_rectangle = int(input("Enter width of the rectangle: "))
    height_rectangle = int(input("Enter height of the rectangle: "))
    
    drawRectangle(rectangle_color, x_center, y_center, width_rectangle, height_rectangle)
    
    drawCircle("black", 0, 0, 50)
    
    turtle.hideturtle()

    

if __name__ == "__main__":
    main()