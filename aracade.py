import sys
from rps8 import rps
from guess_number import  guess_number


def arcade(player_name = "mina"):
    welcome_back = False

    while True:
        if welcome_back	== True:
         print(f"\n{player_name}, welcome to the Arcade!")

        playerChoice = input(f'\nPlease choose a game: \n1 = Rock Paper Scissors \n2 = Guess MyNumber \n\nOr press "x" to exit the Arcade\n ')

        if playerChoice not in ["1","2","x"]:
            print(f"{player_name}, please enter 1, 2, or x")
            return arcade(player_name)
        
        welcome_back = True
        if playerChoice == "1":
            print(f"{player_name}, choose rps")
            rock_paper_scissorss = rps(player_name)
            rock_paper_scissorss()
        elif playerChoice == "2":
            print(f"{player_name}, choose guess number")
            play_guesss = guess_number(player_name)
            play_guesss()
        else:
            print(f"\nSee you next time!")
            sys.exit(f"Bye {player_name}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personalized game experience."
    )

    parser.add_argument(
        "-n","--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    choose_game = arcade(args.name)
    choose_game()

