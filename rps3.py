import sys
import random
from enum import Enum

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    computerChoice = random.choice("123")
    computer = int(computerChoice)

    playerChoice = input('Enter ...\n1 for Rock,\n2 for Paper,\n3 for Scissor:\n\n')

    if playerChoice not in ["1","2","3"]:
        print("You must enter 1,2, or 3")
        return play_rps()
    
    player = int(playerChoice)

    print('\nYou chose' + playerChoice + ".")
    print('Computer chose' + computerChoice + ".")

    if player == RPS.ROCK.value and computer == 3:
        print("You win!")
    elif player == 2 and computer == RPS.ROCK.value:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")
    elif player == computer :
        print("Tie game!😊")
    else:
        print("Python win")

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("🥳🍾🍾🍾")
        print("Thank you for playing \n")
        sys.exit("Bye for now")
play_rps()