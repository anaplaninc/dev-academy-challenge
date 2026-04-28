const readline = require("readline");

class Player{
    constructor(name, unheldScore = 0, score = 0){
        this.name = name;
        this.unheldScore = unheldScore;
        this.score = score;
    }

    resetUnheldScore(){
        this.unheldScore = 0;
    }

    roll(dice){
        const rolled = dice.roll();
        console.log(`${this.name} rolled a ${rolled}`);

        if (rolled === 1){
            this.resetUnheldScore();
            console.log(`${this.name} rolled a 1 and lost unheld score. Turn switches.`);
            return false;
        }

        this.unheldScore += rolled;
        console.log(`${this.name}'s unheld score is now ${this.unheldScore}`);
        return true;
    }

    hold(){
        this.score += this.unheldScore;
        console.log(`${this.name} holds. ${this.unheldScore} points added.`);
        this.resetUnheldScore();
        console.log(`${this.name}'s total score is now ${this.score}`);
    }

    hasWon(){
        return this.score >= 100;
    }
}

class Dice{
    roll(){
        return Math.floor(Math.random() * 6) + 1;
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function ask(question){
    return new Promise((resolve) => {
        rl.question(question, (answer) => {
            resolve(answer.trim().toLowerCase());
        });
    });
}

async function playGame(){
    const player1 = new Player("Jason");
    const player2 = new Player("AnaplanDev");
    const dice = new Dice();
    let currentPlayer = player1;

    console.log("Dice Game started.");
    console.log("Commands: 'r' to roll, 'h' to hold.");

    while (true){
        console.log(`\n${currentPlayer.name}'s turn.`);
        console.log(`Current total score: ${currentPlayer.score}`);
        console.log(`Current unheld score: ${currentPlayer.unheldScore}`);

        const choice = await ask("Roll or Hold? (r/h): ");

        if (choice === "r"){
            const canContinue = currentPlayer.roll(dice);

            if (!canContinue){
                currentPlayer = currentPlayer === player1 ? player2 : player1;
            }
        } else if (choice === "h"){
            currentPlayer.hold();

            if (currentPlayer.hasWon()){
                console.log(`\n${currentPlayer.name} wins with ${currentPlayer.score} points!`);
                break;
            }

            currentPlayer = currentPlayer === player1 ? player2 : player1;
        } else {
            console.log("Invalid input. Please enter 'r' or 'h'.");
        }
    }

    rl.close();
}

playGame();

