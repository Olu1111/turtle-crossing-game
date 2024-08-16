from turtle import *
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.traffic = []
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        chance = r.randint(1, 12)
        if chance == 1 or chance == 3:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(r.choice(COLORS))
            new_car.goto(300, r.randint(-250, 250))
            self.traffic.append(new_car)

    def rush(self):
        traffic = self.traffic
        for car in traffic:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

