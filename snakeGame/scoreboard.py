from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)

    def score_tracker(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

