# 1. IMPORTING RANDOM AND RANDINT TO SPECIFY THE RANGE OF SCORES POSSIBLE FOR DICE ROLL MECHANISM (1-6):
import random
from random import randint

# 2. WELCOME MESSAGE AND CREATING INPUTS FOR PLAYERS 1 & 2:

print("Welcome to my 2 player roll dice game. Let's get started!\n")

player1 = input("Please enter your name player 1: \n")
print(f"Welcome {player1}")

# if not player1:
#    print(f"Ok, we'll call you player 1")


player2 = input("Please enter your name player 2: \n")
print(f"Welcome {player2}")

# if not player2:
#    print(f"Ok, we'll call you player 2 \n")

# 3.STARTING THE GAME, BOTH PLAYERS START ON 0 POINTS :
print(input(f"{player1} will go first, press enter to continue ..."))

player1_game_score = 0
player2_game_score = 0

# 4. DICE ROLLING MECHANIC, FED TO TURN SCORE VARIABLE AND RULE FOR ROLLING A 1:
dice_roll = random.randint(1,6)
turn_score = dice_roll

print(f"You have rolled a: {dice_roll}. And your turn score is {turn_score}.")


if dice_roll == 1:
    print("You rolled a 1. End of turn.")
else:
    print(input(f"Would you like to bank points?, if "))