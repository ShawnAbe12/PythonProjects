from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self,x_cor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x_cor,200)
        self.score = 0
        self.write(self.score, align="center", font= ("Courier",80, "normal"))

    def refresh(self):
        self.write(self.score, align="center", font= ("Courier",80, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh()