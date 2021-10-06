import turtle
import colorgram
from turtle import Turtle, Screen
import random

# colors = colorgram.extract('image.jpg', 30)
# rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new = (r, g, b)
#     rgb.append(new)
# print(rgb)

color_list = [(144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]

turtle.colormode(255)
point = Turtle()
x = -250
y = -230
point.penup()
point.speed("fastest")
point.hideturtle()
for i in range(10):
    point.goto(x , y)
    y += 50
    for j in range(10):
        point.color(random.choice(color_list))
        point.pendown()
        point.dot(20)
        point.penup()
        point.forward(50)

screen = Screen()
screen.exitonclick()