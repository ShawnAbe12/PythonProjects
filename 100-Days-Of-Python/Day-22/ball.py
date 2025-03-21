from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed(0)
        self.penup()
        self.ball_speed = 0.1
        self.x_direction = 1
        self.y_direction = 1

    def move_ball(self):
        new_x = self.xcor() + (10 * self.x_direction)
        new_y = self.ycor() + (10 * self.y_direction)
        self.goto(new_x, new_y)

    def refresh(self):
        self.goto(0,0)
        self.x_direction *= -1
        self.y_direction *= -1
        self.ball_speed = 0.1
