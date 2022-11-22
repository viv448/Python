import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

tim = Turtle()
screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_up_l, "Up")
screen.onkey(paddle.go_down_l, "Down")
screen.onkey(paddle.go_up_r, "w")
screen.onkey(paddle.go_down_r, "s")

is_game_on = True
l_score = 0
r_score = 0

while is_game_on:
    screen.update()
    time.sleep(ball.intensity)
    ball.move()

# detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

        # Detect collision with paddle
    if ball.distance(paddle.right) < 40 and ball.xcor() > 320 or \
            ball.distance(paddle.left) < 40 and ball.xcor() < 320:
        ball.bounce_x()

        # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        l_score += 1

        # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        r_score += 1

    if l_score == 10 or r_score == 10:
        is_game_on = False
        scoreboard.game_over()

screen.exitonclick()

# play_game()
