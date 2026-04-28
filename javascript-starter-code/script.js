'use strict';

// Selecting elements
const score0Element = document.querySelector('#score--0');
const score1Element = document.getElementById('score--1');
const diceElement = document.querySelector('.dice');
const currentScore0Element = document.getElementById('current--0');
const currentScore1Element = document.getElementById('current--1');
const player0Element = document.querySelector('.player--0');
const player1Element = document.querySelector('.player--1');
const player0NameElement = document.getElementById('name--0');
const player1NameElement = document.getElementById('name--1');

//Buttons
const rollBtn = document.querySelector('.btn--roll');
const holdBtn = document.querySelector('.btn--hold');
const resetBtn = document.querySelector('.btn--new');

// Starting conditions
score0Element.textContent = 0;
score1Element.textContent = 0;

//Game Config/Variables

//Stored inside an object so we can access all required game variables using game.(variable name)
const game = {
  players: [
    //Tracks our players, using an array would potentially allow for additional players to be added
    { name: 'Player 2', total: 0 },
    { name: 'Player 2', total: 0 },
  ],
  currentScore: 0, //Tracks the current score
  currentPlayer: 0, //Tracks the index of the current player, which we can use in the 'players' array
  isGameOver: false, //Tracks whether the game is over e.g. has someone won
};

//Game Logic Functions

//Roll function, gives us a random number between 1-6, if 1 switches player and resets current score
//If not a 1, then add the current score and allow user to roll again
function roll() {
  if (game.isGameOver) return; //First we check if the game is finished, if yes, then we don't do anything

  //Get our random number between 1-6
  const randomNum = Math.ceil(Math.random() * 6);
  updateDiceImage(randomNum);

  //Check if we have 'rolled' a 1
  if (randomNum === 1) {
    game.currentScore = 0; //Reset the current score to 0
    //TODO: Switch Player
  } else {
    game.currentScore += randomNum; //Add our randomNum to the currentTotal
  }
  updateScoresUI();
}

//UI Update Functions

//Update to scores to reflect both the current score for the active player, and also the player's total scores
function updateScoresUI() {
  if (game.currentPlayer === 0) {
    currentScore0Element.textContent = game.currentScore;
  } else {
    currentScore1Element.textContent = game.currentScore;
  }

  //Update the player's totals displayed
  score0Element.textContent = game.players[0].total;
  score1Element.textContent = game.players[1].total;
}

//Update the dice elements src using the randomNumber we recieve in the roll function
function updateDiceImage(num) {
  diceElement.src = `../assets/dice-${num}.png`;
}

//UI Interaction/Event Listeners
rollBtn.addEventListener('click', roll); //Assign our roll function to the roll button
