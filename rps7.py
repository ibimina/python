import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        
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

        print(f"\nYou chose  {playerChoice}.")
        print(f'Computer chose {computerChoice}.')

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == RPS.ROCK.value and computer == 3:
                player_wins += 1
                return "You win!"
            elif player == 2 and computer == RPS.ROCK.value:
                player_wins += 1
                return "You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win!"
            elif player == computer :
                return "Tie game!😊"
            else:
                python_wins += 1
                return "Python win"
        
        game_result = decide_winner(player, computer)

        print(game_result)
        
        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer wins count: { str(player_wins)}" )
        print(f"\nPython wins count: {str(python_wins)}")

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
            
    return play_rps

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()