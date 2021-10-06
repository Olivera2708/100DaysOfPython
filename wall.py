from turtle import Turtle


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pensize(2)
        self.penup()
        self.goto(-290, 260)
        self.pendown()
        self.goto(280, 260)
        self.goto(280, -280)
        self.goto(-290, -280)
        self.goto(-290, 260)
