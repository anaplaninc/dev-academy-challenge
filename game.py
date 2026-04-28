#used to randomise the dice roll value
import random

def rolldice():
    diceroll = random.choice(dice)
    print(f'You rolled a {diceroll}!')
    return diceroll


def player1():
    print("Player 1's Turn")

def player2():
    print("Player 2's Turn")
    

def maingame():
    current_state = "player1"
    game_running = True

    while game_running:
        if current_state == "player1":
            current_state = player1()
        elif current_state == "player2":
            current_state = player2()
        

#initialising the two players and assigning their starting score to 0
player1 = 0
player2 = 0

dice = [1,2,3,4,5,6] 
    
print(" Welcome to the Cee's Dice Rolling Game!")


playerinput = input("Type 'yes' to roll the dice or 'no' if you want to change turn:  ").lower()
if playerinput == "yes":
    result = rolldice()
    print(result)
else:
    print("Exiting")









#To run game:
# python3 -u game.py