from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.r_score == 5:
            self.goto(0, 0)
            self.write("GAME OVER, RIGHT PLAYER WON!", align="center", font=("Courier", 20, "normal"))
            return False
        elif self.l_score == 5:
            self.goto(0, 0)
            self.write("GAME OVER, LEFT PLAYER WON!", align="center", font=("Courier", 20, "normal"))
            return False
        else:
            return True

