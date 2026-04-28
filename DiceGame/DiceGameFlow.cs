using DiceGame.Player; 
using DiceGame;

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
       Player currentPlayer = player1;

       int rollScore = 0;
       int currentTurnScore = 0;
       bool gameOver = false;

       while (!gameOver)
        {
            Console.WriteLine($"It is player {currentPlayer.Name}'s turn. Please roll dice by press enter.");
            Console.ReadLine();

            rollScore = Dice.RollDice();

            if (rollScore == 1)
            {
                Console.WriteLine("you rolled a 1, tyou lose all unheld scores and your turn ends.");
                currentTurnScore = 0;
                currentPlayer = currentPlayer == player1? player2: player1;
                continue;
            }

            currentTurnScore += rollScore;

            Console.WriteLine("Choose your option below:");
            Console.WriteLine("1: continue turn");
            Console.WriteLine("2: add unheld score to total score and end turn.");
            string choice = Console.ReadLine();

            if (choice == "2")
            {
                currentPlayer.Score += currentTurnScore;
                if (currentPlayer.Score >= 100)
                {
                    Console.WriteLine($"{currentPlayer.Name} win the game");
                    break;
                }

                currentPlayer = currentPlayer == player1? player2: player1;
                continue;
            }
        }
       
    }
    
}