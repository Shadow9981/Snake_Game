from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 20, "normal"))
