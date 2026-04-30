from random import randint

class Player:
    def __init__(self, name:str):
        self.name = name
        self.score = 0
    
    
if __name__ == "__main__":
    # Initialise Game Parameters
    num_players = 2
    score_to_win = 100
    dice_sides = 6
    
    # Create players
    players = []
    for i in range(1, num_players+1):
        pname = input(f"Enter player {i} name: ")
        if len(pname) == 0:
            pname = f"Player {i}"
        players.append(Player(pname))
    
    
    # Main game loop
    i = 0
    player = players[i]
    unheld_score = 0
    winner = None
    end = False
    
    while end == False:
        print(f"\n{player.name}'s turn (current score {player.score})")
        
        # Roll die
        roll = randint(1, dice_sides)
        unheld_score += roll
        print(f"You rolled {roll}")
        
        # End turn if roll 1
        if roll == 1:
            input("Unlucky (press key to continue)")
            i = (i+1) % num_players
            player = players[i]
            unheld_score = 0
            continue
        else:
            print(f"Your current un-held score is {unheld_score}")
            action = input(f"Do you want to roll again (1) or hold (2)? ")
            # Roll again
            if action == "1":
                continue
            # hold
            else:
                player.score += unheld_score
                # Check win condition
                if player.score >= score_to_win:
                    winner = player
                    end = True
                    break
                else:
                    i = (i+1) % num_players
                    player = players[i]
                    unheld_score = 0
                    continue
            
    # Announce winner and final scores
    print(f"\nThe winner is {winner.name}")
    for player in players:
        print(f"{player.name} ended with {player.score}")