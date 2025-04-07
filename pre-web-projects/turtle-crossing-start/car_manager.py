from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITION = 240


class CarManager:

    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(0,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-Y_POSITION, Y_POSITION))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_distance
            car.goto(new_x, car.ycor())

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT