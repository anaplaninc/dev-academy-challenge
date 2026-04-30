import random

#a player class to keep track of player name and score
class player():
    def __init__(self, name, id):
        self.name = name
        self.held_score = 0
        self.score = 0
        self.id = id

    #a function to get the player name without interacting the instance directly
    def name():
        return player.name
    
    #when a player chooses to hold display a message and then switch players
    def hold(score):
        player.held_score += score
        print(f"You chose to hold a {score}. Your turn is over")
        switch_player(player.id, player.held_score)
    
    #rolling a random number between 1 and 6
    def roll_dice():
        dice_value = random.randint(1, 6)
        if dice_value == 1:
            print("You rolled a 1. Sadly this ends your turn")
            switch_player(player.id, 0)
        return dice_value
    
    #choosing between hold and roll again
    def actions(dice_value):
        choice_1 = "1 - Hold"
        choice_2 = "2 - Roll again"
        choice = input(f"You rolled a {dice_value}! Would you like to {choice_1} or {choice_2}?\n")
        print(choice)
        if choice == 1:
            player.hold()
        elif choice == 2:
            player.roll_dice()
        else:
            print("Please enter 1 for Hold and 2 for Roll again")
            player.actions(dice_value)

# a function to control switching players and checking for win condition
def switch_player(current_player, held_score):
    player = "player"+current_player
    if held_score >= 100:
        print(f"Congratulations {player}! You win with {held_score}!")
    else:
        if current_player == 1:
            current_player = 2
        elif current_player == 2:
            current_player = 1
    print(f"{player.name}, press enter to roll your dice")

#main game logic - plan is to have it linked to the various player class functions
def game():
    print("""Welcome to 'Dice Game', a push your luck game where one player wins when you get to 100 points!
          Each turn the players will roll the dice and have a choice of rolling again or holding.
          If you choose to roll again you have a chance to increase your rolled value but be careful
          IF YOU ROLL A 1 YOU LOSE YOUR CURRENT SCORE AND END YOUR TURN
          Now, to begin, let's get your names.""")
    player1 = player(input("Player 1, please enter your name or how you would like to be called:"), 1)
    player2 = player(input("Now, player 2, please enter your name or how you would like to be called:"), 2)
    input(f"We are now ready to play! {player1.name}, press enter to roll your dice")
    value = player1.roll_dice()
    player1.actions(value)

#calling the main function to start the game
game()
    



    