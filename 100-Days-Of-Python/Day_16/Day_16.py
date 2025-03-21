# import turtle
# from turtle import Turtle, Screen
#
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("Blue")
# timmy.forward(100)
# print(timmy.position())
# timmy.color("Red")
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "r"

print(table)
