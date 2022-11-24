from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scores = ScoreBoard()
screen.listen()


def play_game():
    is_game_on = True
    continue_play = True

    while is_game_on:
        screen.update()
        time.sleep(0.1)

        snake.move()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")

        #collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scores.score_tracker()

        #detect collision with wall
        xcor = snake.head.xcor()
        ycor = snake.head.ycor()
        if xcor < -280 or xcor > 280 or ycor < -280 or ycor > 280:
            # is_game_on = False
            # scores.game_over()
            scores.reset()
            snake.reset()
            food.refresh()

        #detect collision with tail
        for i in snake.snakes_all[1:]:
            if snake.head.distance(i) < 10:
                scores.reset()
                snake.reset()
                food.refresh()
                # is_game_on = False
                # scores.game_over()


play_game()
screen.exitonclick()
# with open("/Users/chiomaamasiatu/Documents/Tutorial/Python/100_days_of_coding/my_file.txt") as file:
#     contents = file.read()
#     print(contents)



