# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
#
# for item in colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#
#     new_colr = (r, g, b)
#
#     rgb_colors.append(new_colr)
#
# print(rgb_colors)

import turtle as t
from turtle import Screen
import random

t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
              (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252),
              (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9),
              (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167),
              (77, 234, 202), (52, 234, 243), (3, 67, 40)]

# for i in range()
tim.setheading(225)
tim.forward(320)
tim.setheading(0)


def hirst_painting(number_of_times):
    for i in range(number_of_times):
        for j in range(10):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)

hirst_painting(10)

screen = Screen()
screen.exitonclick()
