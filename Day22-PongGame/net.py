# from turtle import Turtle

# class Net(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("gray")
#         self.hideturtle()
#         self.penup()
#         self.speed("fastest")
#         self.goto(0, -300)
#         self.left(90)
#         self.left(90)
#         while self.ycor() < 300:
#             self.forward(5)
#             self.pendown()
#             self.forward(20)
#             self.penup()

from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("gray")
        self.pensize(4)
        self.penup()
        self.left(90)
        self.goto(0, -290)
        for i in range(19):
            self.forward(15)
            self.pendown()
            self.forward(15)
            self.penup()
