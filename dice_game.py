# 1. IMPORTING RANDOM AND RANDINT TO SPECIFY THE RANGE OF SCORES POSSIBLE FOR DICE ROLL MECHANISM (1-6):
import random
from random import randint

# 2. WELCOME MESSAGE AND CREATING INPUTS FOR PLAYERS 1 & 2:

print("Welcome to my 2 player roll dice game. Let's get started!\n")

player1 = input("Please enter your name player 1: \n")
print(f"Welcome {player1}")

if not player1:
    print(f"Ok, we'll call you player 1")


player2 = input("Please enter your name player 2: \n")
print(f"Welcome {player2}")

if not player2:
    print(f"Ok, we'll call you player 2 \n")

# 3.

# 4. DICE ROLLING MECHANIC, FED TO TURN SCORE VARIABLE AND RULE FOR ROLLING A 1:
dice_roll = random.randint(1,6)
print(dice_roll)

turn_score = dice_roll


if dice_roll == 1:
    print("End of turn")
else:
    print("Would you like to h")