public class Game {
    Integer score1 = 0;
    Integer score2 = 0;

    // Player turn number for switching turns
    Integer turn = 1;

    public Game(){

    }

    public static void main(String[] args){
        Game game = new Game();
        Player p1 = new Player("Owen", 1);
        Player p2 = new Player("Steven", 2);
        Dice dice = new Dice();
        dice.Roll();

        // Run game allowing each user to roll. Add input functionality.
        while(game.score1 < 100 || game.score2 < 100){
            Integer rollScore = game.takeTurn(dice, p1);
            game.bank(p1, rollScore);
            rollScore = game.takeTurn(dice, p2);
            game.bank(p2, rollScore);
            game.displayGameState();
        }
    }

    // Add turn score to total player score
    public void bank(Player player, Integer turnScore){
        player.totalScore += turnScore;
        if(player.playerNumber == 1){
            score1 += turnScore;
        } else {
            score2 += turnScore;
        }
    }

    public Integer takeTurn(Dice dice, Player player){
        Integer roll = dice.Roll();
        player.turnScore = roll;
        return roll;
    }

    public void displayGameState(){
        System.out.println("Player 1 score is " + score1);
        System.out.println("Player 2 score is " + score2);
    }

    public void resetGame(){

    }

    public void newGame(){

    }
}
