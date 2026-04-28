namespace DiceGame;

public class Dice
{
    private static Random rand = new Random();

    //A static method that give a random number out of given range
    public static int RollDice()
    {
        return rand.Next(1, 7);
    }
}