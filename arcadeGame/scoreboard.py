from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
FONT2 = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(-100, 180)
        self.write("Player 1", align="center", font=FONT2)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)
        self.goto(100, 180)
        self.write("Player 2", align="center", font=FONT2)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        # self.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)
        if self.l_score == 10:
            self.write("GAME OVER! Player 1 won", False, align=ALIGNMENT, font=FONT2)
        else:
            self.write("GAME OVER! Player 2 won", False, align=ALIGNMENT, font=FONT2)

    # def winner(self):
    #     if self.l_score == 10 or self.r_score == 10:

