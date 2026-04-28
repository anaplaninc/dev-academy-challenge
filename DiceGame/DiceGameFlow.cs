using DiceGame.Player; 

namespace DiceGame;

public class DiceGameFlow()
{

    public void Play()
    {
       Console.WriteLine("Please enter first player name:"); 
       string player1Name = Console.ReadLine();
       Console.WriteLine("please enter second player name:");
       string player2Name = Console.ReadLine();

       Player player1 = new Player(player1Name);
       Player player2 = new Player(player2Name);
       
    }
    
}