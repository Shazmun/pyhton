import turtle

color = int(input("Enter 1 for red upper triangle and blue lower triangle.\nEnter 2 for blue upper triangle and red lower triangle: "))

if color == 1:
    c1 = "red"
    c2 = "blue"
else:
    c1 = "blue"
    c2 = "red"
    

outertop_x = 0 
outertop_y = 200
innertop_x= 0
innertop_y= 100
baseleft_x = -100
baseleft_y = 0
baseright_x = 100
baseright_y = 0
#outer triangle
turtle.penup()
turtle.fillcolor(c1)
turtle.begin_fill()
turtle.goto(outertop_x, outertop_y)
turtle.pendown()
turtle.goto(baseleft_x, baseleft_y)
turtle.goto(baseright_x, baseright_y)
turtle.goto(outertop_x, outertop_y)
turtle.end_fill()
#inner triangle
turtle.penup()
turtle.fillcolor(c2)
turtle.begin_fill()
turtle.goto(innertop_x, innertop_y)
turtle.pendown()
turtle.goto(baseleft_x, baseleft_y)
turtle.goto(baseright_x, baseright_y)
turtle.goto(innertop_x, innertop_y)
turtle.end_fill()

turtle.penup()
turtle.goto(-40, -20) 
turtle.pendown()
turtle.write("Two Triangles", font=("Arial", 12, "normal"))
turtle.hideturtle()
