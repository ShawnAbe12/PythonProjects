from turtle import Turtle, Screen
turtle = Turtle()
my_screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_counter_clockwise():
    turtle.left(10)


def turn_clockwise():
    turtle.right(10)


def clear_drwaing():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=turn_counter_clockwise)
my_screen.onkey(key="d", fun=turn_clockwise)
my_screen.onkey(key="c", fun=clear_drwaing)

# turtle.hideturtle()






my_screen.exitonclick()