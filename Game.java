public class Game {
    Integer score1 = 0;
    Integer score2 = 0;

    public Game(){

    }

    public static void main(String[] args){
        Game game = new Game();
        Player p1 = new Player(1);
        Player p2 = new Player(2);
        Dice dice = new Dice();
        dice.Roll();

        while(game.score1 < 100 || game.score2 < 100){
            Integer rollScore = game.takeTurn(dice, p1);
            game.bank(p1, rollScore);
            rollScore = game.takeTurn(dice, p2);
            game.bank(p2, rollScore);
        }
    }

    public void bank(Player player, Integer turnScore){
        player.totalScore += turnScore;
    }

    public Integer takeTurn(Dice dice, Player player){
        Integer roll = dice.Roll();
        player.turnScore = roll;
        return roll;
    }

    public void resetGame(){

    }

    public void newGame(){

    }
}
