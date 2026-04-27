'use strict';
// 4 variables all initialised before the game begins/functions are called

let score = [0,0]; // for player 1 and 2
let turnScore = [0]; // set turnScore to 0
let gameOver = false; // the game shouldnt be over
let currentPlayer = 0; // set the first player to player 1

// function to roll the dice
function rollDice() {
    // if the game is over, dont continue
    if (gameOver == true)
        return;
}

// rolling a random number between 1 - 6 
// random -> round down -> remove all numbers after decimals -> add 1 so it is between 1 and 6
const roll = (Math.floor (Math.random() * 6) + 1);
// update the element with the dice number you rolled
document.getElementById("Dice").textContent() = "You rolled" + roll;
// if 1 is rolled, wipe turnScore to 0
// switch player to other player
// update the screen
if (roll === 1) {
    turnScore = 0;
    switchPlayer();
    // if not 1 (2-6) add to held score
} else {
    turnScore = turnScore + roll;
    updateUI();
}

//function to find each score element and update the screen showing right number
function updateUI(){
    // find the element called total-0 which is player 1 total score, set it to whatever is stored: banked total
    document.getElementById(total-0).textContent = scores [0];
    // same thing for player 2
    document.getElementById(total-1).textContent = scores [1];
    // showing active player only turn score, other player set to 0
if (currentPlayer === 0) {
    document.getElementById(turn-0).textContent = turnScore;
    document.getElementById(turn-1).textContent = 0;

    document.getElementById(turn-0).textContent = 0;
    document.getElementById(turn-1).textContent = turnScore;
}
}

// function to switch the players
function switchPlayer(){
    // if it is player 1 turn, make it player 2
    if (currentPlayer === 0) {
        currentPlayer = 1;
        //if it is player 2 make it player 1
     } else {
            currentPlayer = 0;
        }
        // wipe the turn score to 0
        turnScore = 0;
        // update screen to show new player 
        updateUI;
    }

// function to hold score, adds it to total score
function hold() {
    // if the game is over, dont continue
    if (gameOver === true) {
        return;
    }
    //add the score of the current active player with the turnScore
    scores [currentPlayer] = scores [currentPlayer] + turnScore;
    // if the current active players score is greater than 100, end the game
    if (scores [currentPlayer] >= 100) {
        gameOver = true;
        // display the winner comment
        document.getElementById("dice").textContent = "Winner!";
        // if the current player is the first player, it displays that player 1 won
        if (currentPlayer === 0) {
            alert ("Player 1 wins");
            // if not 1 then must be player 2 so displays that player 2 won
        } else {
            alert ('Player 2 wins');
        }
        return
        }
        // switch to the next player for their turn
        switchPlayer();
}

// function to reset the game
function resetGame() {
    scores = [0,0]; // set the players 1 and 2 
    turnScore = 0; // turned score must be initialised to 0
    currentPlayer = 0; // current player must start at player 1
    gameOver = false; // the game must not be over
    updateUI(); // update the screen 
}