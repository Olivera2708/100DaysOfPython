from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_cor, y_cor)

    def go_up(self):
        if (self.ycor() < 300):
            self.goto(self.xcor(), self.ycor() + 30)

    def go_down(self):
        if (self.ycor() > -300):
            self.goto(self.xcor(), self.ycor() - 30)
