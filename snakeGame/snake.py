from turtle import Turtle, Screen

SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes_all = []
        self.create_snake()
        self.head = self.snakes_all[0]

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("White")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes_all.append(new_snake)

    def reset(self):
        for snake in self.snakes_all:
            snake.goto(1000, 1000)
        self.snakes_all.clear()
        self.create_snake()
        self.head = self.snakes_all[0]

    def extend(self):
        self.add_segment(self.snakes_all[-1].position())

    def move(self):
        for snake in range(len(self.snakes_all)-1, 0, -1):
            new_x = self.snakes_all[snake-1].xcor()
            new_y = self.snakes_all[snake - 1].ycor()
            self.snakes_all[snake].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


