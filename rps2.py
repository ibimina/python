import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:

    computerChoice = random.choice("123")
    computer = int(computerChoice)

    playerChoice = input('Enter ...\n1 for Rock,\n2 for Paper,\n3 for Scissor:\n\n')
    player = int(playerChoice)

    print('\nYou chose' + playerChoice + ".")
    print('Computer chose' + computerChoice + ".")

    if player < RPS.ROCK.value or player > 3:
        sys.exit('You must enter 1, 2, or 3.')

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

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("🥳🍾🍾🍾")
        print("Thank you for playing \n")
        playagain = False