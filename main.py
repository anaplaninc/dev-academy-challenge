def update_score(value):
    # Score update logic goes here
    pass


def roll_dice():
    # Dice rolling logic goes here
    pass


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


def game_loop():
    list_of_players: dict = {}

    list_of_players = initialize_game()

    print(f"Players: {list_of_players}")
    while True:
        # Game logic goes here
        pass


if __name__ == "__main__":
    game_loop()
