from turtle import Turtle
ALIGNMENT = "CENTER"
SCORE_FONT = ("Courier", 80, "normal")
GAME_OVER_FONT = ("Arial", 40, "bold")
WINNER_FONT = ("Arial", 20, "italic")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=SCORE_FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=SCORE_FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self, winner):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)

        self.goto(0, -50)
        self.write(f"{winner} Wins!", align=ALIGNMENT, font=WINNER_FONT)
