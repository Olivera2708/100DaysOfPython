from turtle import Turtle, Screen

point = Turtle()
screen = Screen()


def move_backwards():
    point.back(10)


def move_forwards():
    point.forward(10)


def move_ccwise():
    point.left(10)


def move_cwise():
    point.right(10)


def clear():
    point.clear()
    point.penup()
    point.home()
    point.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_ccwise, "a")
screen.onkey(move_cwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
