// Template for the player object
class Player{
    constructor(score=0, held_score=0, name){
        this.score = score;
        this.held_score = held_score;
        this.name = name;
    }

    rollDice(){
        let currentPlayer = Game.turn
        this.held_score = Math.ceil((Math.random() * 6));
        if (this.held_score.equals(1)){
            Game.changeTurn()
        }else{
            document.getElementById("")
        }
    }

    // adds the held score to the current players current score
    // updates fields
    hold(){

    }
}