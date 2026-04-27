import random


WINNING_SCORE = 100


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.current = 0

    def hold(self):
        self.total += self.current
        self.current = 0

    def reset_current(self):
        self.current = 0

    # def set_name(self, name):
    #     if len(name) <= 0:
    #         self.name = "Computer"
    #     else:
    #         self.name = name

def print_scores(players):
    print()
    for player in players:
        print(f"{player.name}: total={player.total}, current={player.current}")
    print()


def switch_player(active_player):
    return 1 if active_player == 0 else 0


def play_game():
    player_1_name = input(f"What is your name player 1? > ").strip().lower()
    players = [Player(player_1_name), Player("Computer")]
    active_player = 0

    print("Dice game")
    print("Commands: roll, hold, quit")

    while True:
        player = players[active_player]
        print_scores(players)
        command = input(f"{player.name}'s turn > ").strip().lower()

        if command in ("q", "quit", "exit"):
            print("Game ended.")
            return

        if command in ("r", "roll"):
            dice_roll = random.randint(1, 6)
            print(f"{player.name} rolled a {dice_roll}.")

            if dice_roll == 1:
                print(f"{player.name} loses their current points.")
                player.reset_current()
                active_player = switch_player(active_player)
            else:
                player.current += dice_roll

        elif command in ("h", "hold"):
            player.hold()
            print(f"{player.name} holds. Total score is now {player.total}.")

            if player.total >= WINNING_SCORE:
                print(f"{player.name} wins!")
                return

            active_player = switch_player(active_player)

        else:
            print("Please enter roll, hold, or quit.")


if __name__ == "__main__":
    play_game()
