import pandas as pd
from turtle import Turtle, Screen
import time

def init_turtle(turtle):
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0,0)


screen = Screen()
turtle = Turtle()
turtle2 = Turtle()

data = pd.read_csv("50_states.csv")

game_on = True
screen.bgpic("blank_states_img.gif")

init_turtle(turtle)
init_turtle(turtle2)

correct_guesses = []

while game_on:
    turtle2.clear()
    guess = screen.textinput(f"{len(correct_guesses)}/50 States Correct","What's another state name?").lower().title()
    state_guess = data[data["state"] == guess]
    if len(correct_guesses) == 50 or guess == "Win":
        turtle2.write("YOU WIN", font=("Arial",50,"bold"))
        game_on = False
        break
    if state_guess.empty:
        turtle2.write("WRONG", font=("Arial", 20,"bold"))
        time.sleep(0.5)
    else:
        turtle.goto(state_guess["x"].values[0], state_guess["y"].values[0])
        turtle.write(state_guess["state"].values[0])
        if guess not in correct_guesses:
            correct_guesses.append(guess)
            print(correct_guesses)

#states_to_learn.csv

names_list = [ names for names in data["state"] if names not in correct_guesses]
state_dict = {"States":names_list}
# for names in data["state"]:
#     if names not in correct_guesses:
#         state_dict["States"].append(names)
print(state_dict)

state_data = pd.DataFrame(state_dict)
state_data.to_csv("states_to_learn.csv")