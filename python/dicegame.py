import random

def switch_player(playernumber):
    if playernumber == "Player 1":
        playernumber = "Player 2"
    elif playernumber == "Player 2":
            playernumber = "Player 1"
    else: print("error")
    print(" ")
    print(f"Switched to {playernumber}")
    return playernumber


turns = {"Player 1": 0, "Player 2": 0}

def roll_dice():
    return random.randint(1, 6)

def roll1(playernumber):
        print(" ")
        print(f"{playernumber} rolled a 1. No points are given")
        return
    

def __Main__():
    playernumber = "Player 1"
    while turns[f"{playernumber}"]<100:
        print(f"{playernumber}")
        score = roll_dice()
        print(f"You scored a {score}")
        if score == 1:
            roll1(playernumber)
            playernumber = switch_player(playernumber)
        else: 
            potentialscore = turns[f"{playernumber}"] + score
            print("Your options are:")
            print(f"1. Hold: Add {score} to your current score to give you {potentialscore}")
            print(f"2. Roll again if you roll a 1 you will loose all points for this round.")
            userinput = input("Please select on of the above options: ")
            if userinput ==1:
                 turns[f"{playernumber}"]+=score
                 playernumber = switch_player(playernumber)
                 print(f"test: {playernumber}")
                 continue
            if userinput ==2: 
                    print(f"test: {playernumber}")  
                    continue
    print(f"Final scores: {turns}")
    
__Main__()
    