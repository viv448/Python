import turtle
from turtle import Turtle, Screen

X_POS = 350
Y_POS = 0
MOVE_DISTANCE = 20
PADDLE_POSITIONS = [(-350, 0), (350, 0)]


class Paddle:
    def __init__(self):
        self.paddle_holder = []
        self.create_paddle()
        self.left = self.paddle_holder[0]
        self.right = self.paddle_holder[1]

    def create_paddle(self):
        for position in PADDLE_POSITIONS:
            self.add_paddle(position)

    def add_paddle(self, position):
        new_paddle = Turtle(shape="square")
        new_paddle.color("White")
        new_paddle.shapesize(stretch_wid=5, stretch_len=1)
        new_paddle.penup()
        new_paddle.goto(position)
        self.paddle_holder.append(new_paddle)

    def go_up_l(self):
        new_ly = self.left.ycor() + MOVE_DISTANCE
        new_lx = self.left.xcor()
        self.left.goto(new_lx, new_ly)

    def go_up_r(self):
        new_ry = self.right.ycor() + MOVE_DISTANCE
        new_rx = self.right.xcor()
        self.right.goto(new_rx, new_ry)

    def go_down_l(self):
        new_ly = self.left.ycor() - MOVE_DISTANCE
        new_lx = self.left.xcor()
        self.left.goto(new_lx, new_ly)

    def go_down_r(self):
        new_ry = self.right.ycor() - MOVE_DISTANCE
        new_rx = self.right.xcor()
        self.right.goto(new_rx, new_ry)

    # causing all paddles to go down same time
    # def go_down(self):
    #     for paddle in range(0, len(self.paddle_holder)):
    #         new_y = self.paddle_holder[paddle].ycor() - MOVE_DISTANCE
    #         new_x = self.paddle_holder[paddle].xcor()
    #         self.paddle_holder[paddle].goto(new_x, new_y)

