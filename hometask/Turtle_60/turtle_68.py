import random
import turtle
lines = random.randint(1, 30)
for i in range(1, lines):
    right = random.randint(1, 365)
    left = random.randint(1, 365)
    string = random.randint(1, 100)
    choice = random.choice([right, left, string])
    turtle.forward(string)
    turtle.right(right)
    turtle.left(left)
turtle.exitonclick()