from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def update_l_score(self):
        self.l_score += 1
        self.scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.scoreboard()

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER!")
