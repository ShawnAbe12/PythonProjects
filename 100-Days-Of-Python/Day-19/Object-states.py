from turtle import Turtle, Screen
import random


def winner(choice, turtle_color):
    if choice == turtle_color:
        return "won"
    else:
        return "lost"


screen = Screen()
is_race_on = False
screen.setup(width=500,height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
choice = screen.textinput("Make your bet",f"Which turtle will win the race? Enter a color: {colors}")

turtles = []
for i in range(0, 6):
    turtle = Turtle("turtle")
    turtle.speed(0)
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-230, -125 + i * 50)
    turtles.append(turtle)

if choice:
    is_race_on = True

while is_race_on:
    for chosen_turtle in turtles:
        if chosen_turtle.xcor() > 230:
            is_race_on = False
            print(f"You've {winner(choice,chosen_turtle.color()[0])}! The {chosen_turtle.color()[0]} turtle is the winner!")
            break
        chosen_turtle.forward(random.randint(0,20))

screen.exitonclick()