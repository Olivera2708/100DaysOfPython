from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.highest_speed = STARTING_MOVE_DISTANCE
        self.all_speed = [STARTING_MOVE_DISTANCE]

    def crate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def car_levelup(self):
        self.highest_speed += MOVE_INCREMENT
        self.all_speed.append(self.highest_speed)
        

    def move(self):
        for car in self.all_cars:
            car.forward(random.choice(self.all_speed))
        
