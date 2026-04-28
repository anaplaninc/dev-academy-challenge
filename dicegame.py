#Imported random module to generate random numbers for dice rolls
import random


print("Welcome to the Dice Game! First to reach 100 or more points wins. There are 2 players. if a player rolls a 1 they lose any unheld score from that turn and the next player goes." \
      " If a player rolls a 2-6 they can choose to hold their score or roll again. If they hold, their unheld score is added to their total score and the next player goes.")

#Creating variables to store player names and scores
User1 = input("Player 1, please enter your name: ")
User2 = input("Player 2, please enter your name: ")