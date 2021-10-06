from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from net import Net
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
net = Net()

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)

ball = Ball()

screen.listen()
screen.onkeypress(paddle1.go_up, "Up")
screen.onkeypress(paddle1.go_down, "Down")
screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle2.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(paddle1) < 50 and ball.xcor() > 335) or (ball.distance(paddle2) < 50 and ball.xcor() < -335):
        ball.bounce_x()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()