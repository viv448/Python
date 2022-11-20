from turtle import Turtle, Screen, bye, clear, reset, resetscreen, clearscreen
import random


turtle_position = [-100, -60, -20, 20, 60, 100]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def turtles():
    turtle_all = []
    for i in range(0, 6):
        new_turtle = Turtle()
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.shape("turtle")
        new_turtle.goto(x=-230, y=turtle_position[i])
        turtle_all.append(new_turtle)
    return turtle_all


def winner(winning_turtle, user_bet):
    if winning_turtle == user_bet:
        print(f"You've won! The {winning_turtle} turtle is the winner!")
    else:
        print(f"You've lost! The {winning_turtle} turtle is the winner!")


def checking(x):
    if abs(x.xcor()) != -230:
        x.setx(-230)


screen = Screen()
screen.setup(width=500, height=400)


def play_game():
    is_race_on = True
    continue_play = True
    turtle_all = turtles()

    while continue_play:
        winning_turtle = []
        user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ")
        while is_race_on:
            for turtle in turtle_all:
                if turtle.xcor() > 230:
                    is_race_on = False
                    winning_turtle.append(turtle.pencolor())

                rand_distance = random.randint(0, 10)
                turtle.forward(rand_distance)

        winner(winning_turtle[0],
               user_bet)  # to make sure we get the first turtle to cross the line even when there's a
        # draw

        if screen.textinput("continue?", "Do you want to continue playing?: Type 'y' or 'n") == 'y':
            clearscreen()
            # reset()
            is_race_on = True
            turtle_all = turtles()
            for turtle in turtle_all:
                checking(turtle)
        else:
            continue_play = False
    screen.exitonclick()


if screen.textinput("Play game?", "Do you want to play Turtle race? Type 'yes' or 'no': ") == "yes":
    play_game()
