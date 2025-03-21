from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("red")

    def create_snake(self):
        for _ in STARTING_POSITIONS:
            self.new_segment()

    def new_segment(self):
        new_segment = Turtle("square")
        new_segment.hideturtle()
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(0,0)
        self.segments.append(new_segment)
        self.move_segments()
        new_segment.showturtle()

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def move_segments(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def reset(self):

        self.clear_segments()
        self.create_snake()
        self.head = self.segments[0]
        self.head.goto(0,0)

    def clear_segments(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()