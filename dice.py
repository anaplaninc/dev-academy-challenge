import random  

def player_turn(player):
    turn_score = 0  # adds all of the points for the current users turn
    print("it's ",player + "turn!")
    while True:  # keep rolling until the player rolls a 1
        input("Press Enter to roll...")  
        roll = random.randint(1, 6)  
        print("You rolled: " + str(roll))  
        if roll == 1:  # a roll of 1 ends the turn with no points
            print("Rolled a 1! No points this turn.") 
            return 0  # gets rid of all points made so far by player
        turn_score = turn_score + roll 
        print("Turn score: " + str(turn_score))  
        choice = input("Roll again or hold? (roll/hold): ")
        if choice == "hold": 
            return turn_score  


def dicegame():  
    scores = {"Player 1": 0, "Player 2": 0}  # track each player's total score, use hashmap for fast lookup
    while True: 
        for player in scores:  
            turn_result = player_turn(player)
            if turn_result == 0:
                scores[player] = 0  # rolled a 1, reset total score
            else:
                scores[player] = scores[player] + turn_result
            print(player + " total: " + str(scores[player]))  # display the updated total
            if scores[player] >= 100:  
                print(player + " wins!") 
                return  


dicegame() 



