from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("dodger blue")
        self.speed("fastest")
        x_cor = random.randint(-280, 270)
        y_cor = random.randint(-270, 250)
        self.goto(x_cor, y_cor)
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-280, 270)
        y_cor = random.randint(-270, 250)
        self.goto(x_cor, y_cor)

