import sys
import random

def guess_number(playerOne= "mina"):
     game_count = 0
     player_score = 0

     def play_guess_number():
         nonlocal playerOne
         nonlocal game_count
         nonlocal player_score

         computerChoice = random.choice("123")
         computer = int(computerChoice)

         playerChoice = input(f'\n{playerOne}, guess which number I\'m thinking of...1, 2, or 3\n')

         if playerChoice not in ["1","2","3"]:
            print(f"{playerOne}, please enter 1, 2, or 3")
            return play_guess_number()
         
         player = int(playerChoice)

         print(f"\n{playerOne}, You chose  {playerChoice}.")
         print(f'I was thinking about the number {computer}.')

         
         def decide_winner(player, computer):
            nonlocal playerOne
            nonlocal player_score

            if player == computer :
                player_score += 1
                return "You win!"
            else:
                return f"\nSorry {playerOne} Better luck next time"
        
         game_result = decide_winner(player, computer)
         
         print(game_result)
        
         nonlocal game_count

         game_count += 1

         print(f"\nGame count: {game_count}")
         print(f"\n{playerOne}'s count: {player_score}" )
         print(f"\nYour winning percent: { player_score / game_count:2%}")

         print(f"\nPlay again {playerOne}?")

         while True:
            playagain = input("\nY for Yes or \nQ to Quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

         if playagain.lower() == "y":
                return play_guess_number()
         else:
                print("🥳🍾🍾🍾")
                print("Thank you for playing \n")
                if __name__ == "__main__":

                    sys.exit(f"Bye {playerOne}!")
                else:
                    return	
                
     return play_guess_number


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

    play_guess = guess_number(args.name)
    play_guess()