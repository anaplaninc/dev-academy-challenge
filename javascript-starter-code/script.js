'use strict';

// Selecting elements
const score0Element = document.querySelector("#score--0");
const score1Element = document.getElementById("score--1");
const diceElement = document.querySelector(".dice");

// Starting conditions
score0Element.textContent = 0;
score1Element.textContent = 0;
diceElement.classList.add("hidden");

// Setting button functions
document.getElementsByClassName("btn--new").onclick= gameInit;

// Initialise Game
function gameInit() {
    let playerOneName = document.getElementById("name--1").value;
    let playerTwoName = document.getElementById("name--2").value;

    let game = new Game(playerOneName, playerTwoName);
}

