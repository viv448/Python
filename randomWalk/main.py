import turtle
from turtle import Turtle, Screen
import random

tim = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rand_color = (r, g, b)
    return rand_color


directions = [0, 90, 180, 270]

for _ in range(200):
    tim.width(15)
    tim.speed("fast")  # fastest, fast, normal, slow
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
