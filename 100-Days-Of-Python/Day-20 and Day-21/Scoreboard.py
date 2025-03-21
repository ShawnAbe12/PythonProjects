from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", "r") as file:
            self.high_score = file.read()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}",align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.refresh()

    def reset(self):

        if self.score > self.high_score:
            with open("high_score.txt","w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER ",align="center", font=("Arial", 20, "normal"))
