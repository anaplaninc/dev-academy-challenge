# Dice Game project brief
## Overview 

You will build a 2-player dice game. Players take turns rolling a die and trying to be the first to reach a total score of 100 or more. 

You can implement this in any programming language. 
if you’d like, we can provide starter HTML/CSS for a JavaScript version - just ask. 

You may also choose to begin with a flowchart to help map out the game states and transitions - again, just ask if you’d like support with this. 

## Game Rules 

### Objective 

Be the first player to reach a total score of 100 or more. 

### Turn flow 

On a player’s turn: 

1. The player rolls the die. 

2. After each roll, the player chooses to either: 

    1. Hold: add the points from their current un-held score to their total held score, then end their turn (switch to the other player). 

    2. Roll again: keep playing their turn to try and increase their un-held score. 

### Rolling a 1 

If the player rolls a 1: 

- They lose any un-held score from that turn 

- Their turn ends immediately 

- Play switches to the other player 

### Winning the game 

The game ends when a player’s total score reaches 100 or more. 

## What your solution should include 

At a minimum, your solution should demonstrate: 

- Two players taking turns 

- Each player should be able to enter their name or play under predefined names of “Player 1” and “Player 2” 

- A dice roll mechanic (1–6) 

- Tracking: 

    - Current turn score (un-held) 

    - Total held score per player 

- Hold action to bank points and switch turns 

- Rolling a 1 reset the turn score and switches turns 

- Win condition at 100+ held score 

## Suggested approach (optional) 

If helpful, consider breaking the problem into parts: 

- Data/state model (players, scores, current player, game status) 

- Turn logic (roll, hold, switch) 

- User interaction (CLI prompts or UI buttons) 

- Display/output (scores, whose turn, winner message) 

- Edge cases (prevent rolling after game ends, reset/new game) 

## What we’re assessing 

We’re not looking for a perfect or “fancy” solution. We’re interested in: 

- Clear thinking and problem decomposition 

- Correct handling of game rules and state 

- Readable, maintainable code 

- A strong ReadMe File and comments in the code 

- Your ability to explain decisions (if asked) 

- How you handle uncertainty and make reasonable assumptions 

 