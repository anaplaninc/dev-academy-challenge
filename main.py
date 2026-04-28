import random


def roll_dice() -> int:
    dice_value: int = 0
    dice_value = random.randint(1, 6)
    return dice_value


def is_game_over():
    # Game over condition logic goes here
    pass


def create_players(amount: int) -> dict:
    players_dict: dict = {i: 0 for i in range(amount)}
    return players_dict


def initialize_game():
    player_amount: int = 0
    dict_of_players: dict = {}
    while True:
        print("How many players are playing?")
        try:
            player_amount: int = int(input())
            if 0:
                print("Number of players must be greater than 0.")
                # quit()
            else:
                dict_of_players = create_players(player_amount)
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            pass
    return dict_of_players


def play_turn(player: int):
    print(f"Player {player}'s turn.")
    input("Press Enter to roll the dice...")
    dice_value: int = roll_dice()
    print(f"Player {player} rolled a {dice_value}.")


def game_loop():
    list_of_players: dict = {}

    list_of_players = initialize_game()
    player: int = 0
    while True:
        print(f"Player {player}'s turn.")
        while True:
            input("Press Enter to roll the dice...")
            dice_value: int = roll_dice()
            print(f"Player {player} rolled a {dice_value}.")
            if dice_value == 1:
                print("You rolled a 1! Your turn is over.")
                player = (player + 1) % len(list_of_players)
                return player
            else:
                print(
                    "You rolled a number other than 1! You can choose to roll again or hold."
                )
                choice: str = input("Enter 'r' to roll again or 'h' to hold: ").lower()
                # hold
                if choice == "h":
                    print(f"Player {player} holds. Ending turn.")
                    list_of_players[player] += dice_value
                    player = (player + 1) % len(list_of_players)
                    break
                # roll again
                elif choice == "r":
                    continue
                else:
                    print("Invalid choice. Please enter 'r' or 'h'.")
        if is_game_over():
            print("Game over!")
            break


if __name__ == "__main__":
    game_loop()
