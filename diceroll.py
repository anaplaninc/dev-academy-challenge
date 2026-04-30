import random
player_name1 = input("What is your name? ")
player_name2 = input("What is your name? ")

def welcome( name ):
    print(f"Welcome, {name}!")# This function takes a name as an argument and prints a welcome message.

    print
def roll_dice( sides=6 ):#shows the number of sides on the dice, default is 6
    return random.randint(1, 6)
if __name__ == "__main__":
    print(roll_dice())        # one 6-sided dice


def play_turn( player ):
    input(f"{player}, press Enter to roll the dice...") 
    roll = roll_dice()
    print(f"{player} rolled a {roll}!")
    return roll

def score_points(param1, param2=None):
    raise NotImplementedError

def play_to_100( player1, player2 ):
    score1 = 0
    score2 = 0
    while score1 < 100 and score2 < 100:# taking turns until one player reaches 100 points
        score1 += score_points(play_turn(player1), score1)
        print(f"{player1}'s total score: {score1}")
        if score1 >= 100:
            break
        score2 += score_points(play_turn(player2))
        print(f"{player2}'s total score: {score2}")
    if score1 >= 100:
        print(f"{player1} wins!")
    else:
        print(f"{player2} wins!")
        

    