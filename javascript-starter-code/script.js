'use strict';

// Selecting elements
const score0Element = document.getElementById("score--0");
const score1Element = document.getElementById("score--1");
const diceElement = document.querySelector(".dice");
const current0Element = document.getElementById('current--0');
const current1Element = document.getElementById('current--1');

// Starting conditions
score0Element.textContent = 0;
score1Element.textContent = 0;
current0Element.textContent = 0;
current1Element.textContent = 0;
diceElement.classList.add("hidden");
var currentPlayer = current0Element;

// Rolls dice and adds the number to the current score before being held
const rollDice = () => {
    const minCield = Math.ceil(1);
    const maxFloored = Math.floor(6)
    const score = Math.floor(Math.random() * (maxFloored - minCield + 1) + minCield)

    // Wanted to add code here to implemente the visual dice asset to show the score rolled

    currentPlayer.textContent = parseInt(currentPlayer.textContent) + score;
    checkValidScore(score);
}; 

// Ensures the player didn't roll a 1 and if they did it 0's their score and resets switches the player
function checkValidScore(score){
    if(score == 1){
        currentPlayer.textContent = 0;
        currentScore = 0;
        if(currentPlayer == current0Element){
            currentPlayer = current1Element;
        }else{
            currentPlayer = current0Element
        }
    }
}

// Will Reset all players scores as well as the score being held
const resetScores = () => {
    score0Element.textContent = 0;
    score1Element.textContent = 0;
    current0Element.textContent = 0;
    current1Element.textContent = 0;
}

const holdScore = () => {
    if (currentPlayer == current0Element){
        score0Element.textContent = parseInt(current0Element.textContent) + parseInt(score0Element.textContent);
        currentPlayer.textContent = 0;
        checkWinCondition(parseInt(score0Element.textContent));
        currentPlayer = current1Element;
    }else{
        score1Element.textContent = parseInt(current1Element.textContent) + parseInt(score1Element.textContent);
        currentPlayer.textContent = 0;
        checkWinCondition(parseInt(score1Element.textContent));
        currentPlayer = current0Element;
    }
    currentScore = 0;
}

// Checks if the player has reached the win condition and changes their score to say winner!
function checkWinCondition(score) {
    if (score >= 100)[
        currentPlayer.textContent = "Winner"
    ]
}

// Button event listeners to check when buttons are clicked and apply the relevant listetners
document.getElementById('btn-new').addEventListener("click", resetScores);

document.getElementById('btn-roll').addEventListener("click", rollDice);

document.getElementById('btn-hold').addEventListener("click", holdScore);