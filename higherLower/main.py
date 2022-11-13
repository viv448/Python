"""
import files and libraries needed
"""
from art import logo, vs
from game_data import data
import os
import random

print(logo)


def play_game():
    continue_game = False
    answer_count = 0
    games_played = 0
    prev_data = {}

    while not continue_game:
        # generate random account from the game data
        data_b = random.choice(data)

        if answer_count > 0:
            data_a = prev_data
        else:
            data_a = random.choice(data)

        if data_b == data_a or data_b["follower_count"] == data_a["follower_count"]:
            data_b = random.choice(data)

            # format the account data into printable format

        def format_data(account):
            """takes the account data and returns it in printable format"""
            name = account["name"]
            desc = account["description"]
            country = account["country"]
            return f"{name}, a {desc}, from {country}."

        print(f"Compare A: {format_data(data_a)}\n")
        print(vs)
        print(f"\nAgainst B: {format_data(data_b)}\n")

        # ask user for a guess
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # get highest follower count from the data
        def check_followers(data1, data2):
            answer = ""

            if data1["follower_count"] > data2["follower_count"]:
                answer = "A"
            else:
                answer = "B"
            return answer

        games_played += 1

        # give user feedback and score keeping
        if guess == check_followers(data_a, data_b):
            answer_count += 1
            os.system("clear")
            print(f"\nYou're right! Current score is: {answer_count} out of {games_played}\n")
            # make account at position B become the next account at position A
            prev_data = data_b

        else:
            print(f"\nSorry, that's wrong. Final score: {answer_count} out of {games_played}")

            # make the game repeatable
            if input("\nDo you want to continue playing? Type 'yes' or 'no': ").lower() == 'yes':
                os.system("clear")
                answer_count = 0
                games_played = 0
            else:
                continue_game = True


# run the function and play the game
if input("Do you want to play Higher Lower? Type 'yes' or 'no': ").lower() == "yes":
    play_game()

