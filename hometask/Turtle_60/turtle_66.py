import turtle
import random
for i in range(0, 8):
    colour = random.choice(["Black", "yellow", "blue", "red", "green"])
    turtle.color(colour)
    turtle.forward(50)
    turtle.right(45)
turtle.exitonclick()