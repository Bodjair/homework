import turtle
for i in range(0, 4):
    turtle.color("red", "brown")
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.forward(200)
turtle.pendown()
for i in range(0, 4):
    turtle.color("blue", "yellow")
    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.forward(-400)
turtle.pendown()
for i in range(0, 4):
    turtle.color("yellow", "blue")
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()