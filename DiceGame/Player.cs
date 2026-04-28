namespace DiceGame;

public class Player()
{
    public string Name { get; set; }
    public int TotalScore { get; set; }

    public Player(string name)
    {
        Name = name;
        TotalScore = 0;
    }
}