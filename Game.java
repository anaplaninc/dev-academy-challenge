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

        }
    }

    public void bank(Player player){
        
    }

    public void takeTurn(Dice dice, Player player){
        Integer roll = dice.Roll();
        player.turnScore = roll;
    }
}
