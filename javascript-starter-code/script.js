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
const rollBtn = document.getElementById('btn--roll')
const holdBtn = document.getElementById('btn--hold')
const resetBtn = document.getElementById('btn--new')

// Starting conditions
score0Element.textContent = 0;
score1Element.textContent = 0;
