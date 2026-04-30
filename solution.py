import random

def roll_dice():
    dice = random.randint(1,6)
    print("You rolled " + str(dice))
# rolling dice and displaying to user

    if dice == 1:
        dice == 0
    # if player rolles a 1 then they losses their turn

    return dice

def player (players):
    players = [1, 2]
    player1_name = input("Player 1")
    player2_name = input("Player 2")
    player1_score = 0
    player2_score = 0 
    currentPlayer = 1
    currentPlayer_score = player1_score
    #start with player 1


# i want to uses an list for my player
# swapping between them and using that to streamline the code                                                                                                                                                           cffffffffffffffffffffff            c                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
# right now i cant find a way to do this and store both players scores/names


def game (dice, players, player1_name, player2_name, player1_score, player2_score, currentPlayer, currentPlayer_score):
    score = 0 


    while player1_score or player2_score >= 100:
        #player 1
        roll_dice
        score = dice
        print(player1_name + "Rolled a " + player1_score)
        # displaying current scores
        
        if input("reroll"):
            player1_score = player1_score + dice
            print(player1_name + "Current score is" + player1_score)
        else:
            players = players.index +1
        #place holder as i work out how to switch between players



        #player 2
        roll_dice
        player2_score = player2_score + dice
        print(player2_name + "Current score is" + player2_score)

        if input("reroll"):
            player2_score = player2_score + dice
            print(player2_name + "Current score is" + player2_score)
        else:
            players = players.index +1


    
    if player1_score >= 100:
        print(str(player1_name) + "Wins!")
    elif player2_score >= 100:
        print(str(player2_name) + "Wins!")

    #displaying winner
        


    