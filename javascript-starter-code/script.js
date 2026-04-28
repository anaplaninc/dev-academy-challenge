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
const rollBtn = document.getElementById('btn--roll');
const holdBtn = document.getElementById('btn--hold');
const resetBtn = document.getElementById('btn--new');

// Starting conditions
score0Element.textContent = 0;
score1Element.textContent = 0;

//Game Config/Variables
//Stored inside an object so we can access all required game variables using game.(variable name)
const game = {
  players: [ //Tracks our players, using an array would potentially allow for additional players to be added
    { name: 'Player 2', total: 0 },
    { name: 'Player 2', total: 0 },
  ],
  currentScore: 0, //Tracks the current score
  currentPlayer: 0, //Tracks the index of the current player, which we can use in the 'players' array
  isGameOver: false, //Tracks whether the game is over e.g. has someone won
};
