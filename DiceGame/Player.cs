namespace DiceGame;

public class Player()
{
    //Properties that the player class hold
    public string Name { get; set; }
    public int TotalScore { get; set; } = 0;

    //constructor that requires a string to define name;
    public Player(string name)
    {
        Name = name;
        TotalScore = 0;
    }
}