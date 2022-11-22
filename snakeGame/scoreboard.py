from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)

    def score_tracker(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

