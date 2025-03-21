from turtle import Turtle
x_pos = 380
STARTING_POSITIONS = [(-x_pos,0),(-x_pos,20),(-x_pos,40)]

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(pos[0],pos[1])

    def create_paddle(self):
        pass
        # for pos in STARTING_POSITIONS:
        #     new_segment = Turtle("square")
        #     new_segment.hideturtle()
        #     new_segment.color("white")
        #     new_segment.setheading(90)
        #     new_segment.penup()
        #     new_segment.goto(pos)
        #     self.segments.append(new_segment)
        #     # new_segment.showturtle()
        # for seg in self.segments:
        #     seg.showturtle()

    def up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

