from turtle import Screen
from snake import Snake
from food import Food
from wall import Wall
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

wall = Wall()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 260 or snake.segments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1::]:
        if snake.segments[0].distance(segment) < 7:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
