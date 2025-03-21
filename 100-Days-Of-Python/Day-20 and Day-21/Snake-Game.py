import time
from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_on = True

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

##Dev Tools
screen.onkey(snake.new_segment,"a")

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move_segments()

    if snake.head.distance(food) < 15:
        snake.new_segment()
        food.refresh()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()