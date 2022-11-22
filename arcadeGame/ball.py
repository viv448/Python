from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.x_position = 10
        self.y_position = 10
        self.intensity = 0.1

    def move(self):
        new_x = self.xcor() + self.x_position
        new_y = self.ycor() + self.y_position
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_position *= -1

    def bounce_x(self):
        self.x_position *= -1
        if self.intensity * 0.9 < 0:
            self.intensity = 0.1
        else:
            self.intensity *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.intensity = 0.1
        self.bounce_x()


