public class Game {
    Integer score1 = 0;
    Integer score2 = 0;

    public static void main(String[] args){
        Player p1 = new Player(1);
        Player p2 = new Player(2);
        Dice dice = new Dice();
        dice.Roll();
    }

    public void takeTurn(){
        
    }
}
