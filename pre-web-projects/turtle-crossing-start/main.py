import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")
game_loop = 0
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
            break
    if player.ycor() > player.finish_line:
        scoreboard.level_up()
        car_manager.speed_up()
        player.restart()

    car_manager.move()
screen.exitonclick()


