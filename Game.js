// stores the state of the game
class Game{
    constructor(player1, player2) {
        this.player1 = new Player(player1);
        this.player2 = new Player(player2);

        // Odd turns indicate player 1's turn
        // Even turns indicate player 2's turn
        this.turn = 1;
    }

    static changeTurn(){
        this.turn++;
    }

}