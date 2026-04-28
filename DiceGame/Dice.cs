namespace DiceGame;

public class Dice
{
    private static Random rand = new Random();

    public static int RollDice()
    {
        return rand.Next(1, 7);
    }
}