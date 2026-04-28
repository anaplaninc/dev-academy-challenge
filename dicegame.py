#Imported random module to generate random numbers for dice rolls
import random


print("Welcome to the Dice Game! First to reach 100 or more points wins. There are 2 players. if a player rolls a 1 they lose any unheld score from that turn and the next player goes." \
      " If a player rolls a 2-6 they can choose to hold their score or roll again. If they hold, their unheld score is added to their total score and the next player goes.")

#Creating variables to store player names and scores
User1 = input("Player 1, please enter your name: ")
User2 = input("Player 2, please enter your name: ")

#Initializing scores for both players
score1 = 0
score2 = 0

#Main game loop continues until one of the players reaches 100 or more points
while score1 < 100 and score2 < 100:
    input(f"{User1}, press Enter to roll the dice.")
    roll1 = random.randint(1, 6)
    print(f"{User1} rolled a {roll1}.")
    score1 += roll1
    print(f"{User1}'s current score: {score1}")

    if score1 >= 100:
        print(f"Congratulations {User1}! You win with a score of {score1}!")
        break 

#user2's turn to roll the dice and update score  
    input(f"{User2}, press Enter to roll the dice.")
    roll2 = random.randint(1, 6)
    print(f"{User2} rolled a {roll2}.")
    score2 += roll2
    print(f"{User2}'s current score: {score2}")

    if score2 >= 100:
        print(f"Congratulations {User2}! You win with a score of {score2}!")
        break