from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((350, 0))
paddle2 = Paddle((-360, 0))

L_score = Scoreboard(-100)
R_score = Scoreboard(100)

ball = Ball()

game_on = True

screen.listen()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    if (ball.distance(paddle2) < 50 and ball.xcor() < -320) or (ball.distance(paddle) < 50 and ball.xcor() > 320):
        ball.x_direction *= -1
        # ball.y_direction *= -1
        ball.ball_speed *= 0.9

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_direction *= -1

    if ball.xcor() > 380:
        ball.refresh()
        L_score.increase_score()

    if ball.xcor() < -380:
        ball.refresh()
        R_score.increase_score()

    ball.move_ball()

screen.exitonclick()
