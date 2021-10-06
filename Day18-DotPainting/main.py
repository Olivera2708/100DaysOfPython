import turtle
from turtle import Turtle, Screen
import random

### square
# point = Turtle()
# for i in range(0, 3):
#     point.forward(100)
#     point.left(90)
# point.forward(100)

### dashed lines
# point = Turtle()
# for i in range(15):
#     point.pendown()
#     point.forward(10)
#     point.penup()
#     point.forward(10)

### shapes
# colors = ["powder blue", "medium spring green", "khaki", "light salmon", "tomato", "light pink", "orchid"]
# point = Turtle()
# line = 3
# for i in range(7):
#     point.pencolor(colors[i])
#     angle = 360 / line
#     for i in range(line):
#         point.forward(50)
#         point.right(angle)
#     line += 1

### random walk
# colors = ["powder blue", "medium spring green", "khaki", "light salmon", "tomato", "light pink", "orchid"]
# choose = [0, 90, 180, 270]
# point = Turtle()
# point.pensize(10)
# point.speed("fastest")
# for i in range(200):
#     point.color(random.choice(colors))
#     point.left(random.choice(choose))
#     point.forward(25)

### random color rgb
# choose = [0, 90, 180, 270]
# point = Turtle()
# turtle.colormode(255)
# point.pensize(10)
# point.speed("fastest")
# for i in range(200):
#     point.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     point.left(random.choice(choose))
#     point.forward(25)

### spirograph
# turtle.colormode(255)
# point = Turtle()
# point.speed("fastest")
# for i in range(72):
#     point.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     point.left(5)
#     point.circle(70)
# screen = turtle.Screen()
# screen.exitonclick()