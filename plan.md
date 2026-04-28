# Game Variables Required
Players - name, totalScore - Player Name, their total score
currentScore - Current rolled accumulative score
currentPlayer - Current player 'rolling'
isGameOver - Is the game over/has someone reach 100 points

# Game Logic
Roll Dice - Add to current total, or if 1 remove current total and switch player
Hold - Add to player's total, reset current total, switch player
Reset Game - Reset all variables to default
Switch Player - Switch the the other player

# UI Updates
Update Dice
Update UI - We can update both the player's total score and the game's current score together.
Update Player Name/s

# UI Interactions/Event Listeners
Roll Button - Roll Dice()
Hold Button - Hold()
Reset Game Button - Reset Game()
Player Name Inputs - Update Player Name()