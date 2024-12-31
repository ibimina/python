import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# RSP.ROCK
# RSP["ROCK"]
# RSP[1]
# RSP.ROCK.value

# value = input('Please enter a value:\n')
# print(value)

print("")
computerChoice = random.choice("123")
computer = int(computerChoice)

playerChoice = input('Enter ...\n1 for Rock,\n2 for Paper,\n3 for Scissor:\n\n')
player = int(playerChoice)

print('')
print('You chose' + playerChoice + ".")
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