import turtle
import turtle as t
import heroes
import villains
from random import randint,choice
# the * imports everything in the module, but it is not usually used because it makes the readability confusing
def choose_direction(direction):
    return choice(direction)
def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    my_tuple =(r, g, b)
    return my_tuple
def draw_circles(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
        print(timmy.heading())



timmy = t.Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")
num = 30
num_of_sides = 3
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']
directions = [0,90,180,270]

draw_circles(30)



# for i in range(200):
#     timmy.color(random_color())
#     timmy.forward(num)
#     timmy.setheading(choose_direction(directions))



# for i in range(3,11):
#     timmy.color(random.choice(color))
#     for j in range(0,i):
#         timmy.forward(30)
#         timmy.right(360/i)
#

# for i in range(36):
#
#     timmy.forward(num)
#     timmy.left(num)
#     timmy.penup()
#     timmy.forward(num)
#     timmy.pendown()


#
# print(heroes.gen())
# print(villains.genarr(5))

screen = t.Screen()
screen.exitonclick()





