import random

class DiceGame:
    def __init__(self):
        self.current_player = 'player1'
        self.p1_score = 0
        self.p2_score = 0
        self.turn_score = 0
        self.gameover = False
        self.winner = None
        
    def switch_player(self):
        self.turn_score = 0
        if self.current_player == 'player1':
            self.current_player = 'player2'
            return "Player 2's turn"
        else:
            self.current_player = 'player1'
            return "Player 1's turn"
            
            
    def roll_dice(self):
        if self.gameover:
            return "game is over, illegal move"
        roll_value = random.randint(1,6)
        if roll_value == 1:
            self.turn_score = 0
            self.switch_player()
            return f"{self.current_player} has rolled a 1 and lost their turn score"
        
        self.turn_score += roll_value
        return f"{self.current_player} rolled {roll_value} and their total score is now {self.turn_score} "
    
    def hold_dice(self):
        if self.gameover:
            return "game is over, illegal move"
        
        if self.current_player == 'player1':
            self.p1_score += self.turn_score
            
            if self.p1_score >= 100:
                self.gameover = True
                self.winner = 'player1'
                return "player 1 wins"
        else:
            self.p2_score += self.turn_score
            
            if self.p2_score >= 100:
                self.gameover = True
                self.winner = 'player2'
                return "player 2 wins"
            
    def display_scores(self):
        return {
            "current_player": self.current_player,
            "turn_score": self.turn_score,
            "player1_score": self.p1_score,
            "player2_score": self.p2_score,
            "winner": self.winner
        }
        
        
game = DiceGame()
print(game.display_scores())
print(game.roll_dice())
print(game.hold_dice())
print(game.display_scores())
print(game.roll_dice())

print(game.hold_dice())

print(game.display_scores())

print(game.roll_dice())
print(game.hold_dice())

print(game.display_scores())