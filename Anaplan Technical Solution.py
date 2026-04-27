# Import modules
import random

CHOICES = ("HOLD", "ROLL AGAIN")

# Choose names for a given number of players
def pick_names(player_count):
    # Initialise variables
    player_names = {}
    scores = {}

    # Loop through each player
    for player_num in range(1, player_count + 1):
        # Ask for the name
        entered_name = input(f"What is Player {player_num}'s name? (PRESS ENTER FOR DEFAULT): ")
        
        # If no input is entered, set the input to be the default
        if len(entered_name) == 0:
            entered_name = "Player " + str(player_num)

        # Add the player names to the dictionary and initialise the score
        player_names["Player " + str(player_num)] = entered_name
        scores["Player " + str(player_num)] = 0
    
    return scores, player_names

# Increment to the next player, looping back to the start if the end is reached
def increment_player(current_player, player_count):
    # Increment the current player
    current_player += 1
    
    # If the current player is beyond the number of players in the game
    if current_player > player_count:
        # Go back to player 1
        current_player = 1

    # Return the current player
    return current_player
        
def main():
    # Number of players
    player_count = 4

    # Get the preferred names and initialised scores
    scores, player_names = pick_names(player_count)
    
    # Initialise the playing flag
    playing = True

    # Starting with player 1
    current_player = 1

    while playing:
        # Roll a 6-sided dice
        roll = random.randint(1, 6)

        # Get the current player's prevered name
        player_name = player_names["Player " + str(current_player)]
        
        # Tell the player it is their turn
        print(f"{player_name}'s turn...")

        # If 1 is rolled, the value of the current player gets reset
        if roll == 1:
            # Reset this player's score
            scores["Player " + str(current_player)] = 0
            print(f"{current_player} rolled a 1 and went down to 0 points!")
            
            # Increment current player
            current_player = increment_player(current_player, player_count)

        # Otherwise
        else:
            # Increment the current player's score
            scores["Player " + str(current_player)] += roll
            player_score = scores["Player " + str(current_player)]
            
            # If player's score is 100, this player wins
            if player_score >= 100:
                print(f"{player_name} WINS with {player_score} points")

                # Set a flag to check whether the choice is valid
                valid_choice = False

                # Until a valid input is entered
                while valid_choice == False:
                    # Ask the user if they would like to play again
                    choice = input("Play again? (Yes/No): ")

                    # Account for variations in how it was typed
                    choice = choice.upper().replace("\"", "").strip()
                    
                    # When the user wants to play again
                    if choice == "YES":
                        valid_choice = True

                        # Reset the current player to be 1
                        current_player = 1

                        # TODO: Fix score reset as fails to go back to 0 correctly
                        # Reset each player score back to 0
                        for player in scores.keys():
                            scores[player] = 0


                    # When the user does not want to play again
                    elif choice == "NO":
                        valid_choice = True
                        # End the game
                        print("THANKS FOR PLAYING!!!!")
                        playing = False
                        return 0
                    
                    # Inform the user more clearly if they have not entered a valid input
                    else:
                        print("Invalid choice, please type either \"Yes\" or \"No\"")

            # Output what the current player rolled
            print(f"{player_name} rolled a {roll} and now has {player_score} points!")

            # Set a flag to check whether the choice is valid
            valid_choice = False

            # Continue asking until a valid input has been entered
            while valid_choice == False:
                # Ask for the user's choice
                choice = input(f"{player_name}, would you like to \"Hold\" or \"Roll again\"? ")

                # Account for variations in how it was typed
                choice = choice.upper().replace("\"", "").strip()

                # If the choice is valid
                if choice in CHOICES:
                    # Update the flag
                    valid_choice = True
                    
                    # If hold is selected then bank the points and switch to the next player
                    if choice == "HOLD":
                        print(f"{player_name} held and now has {player_score} points stored")
                        
                        # Increment the current player
                        current_player = increment_player(current_player, player_count)
                        

                # If invalid, then inform the user more clearly of the options
                else:
                    print("Invalid choice, please select either \"Hold\" or \"Roll again\"")

# Run the game   
if __name__ == "__main__":
    main()