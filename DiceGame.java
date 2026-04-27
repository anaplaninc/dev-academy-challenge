
import java.util.Scanner;


class Main {

    public static void main(String[] args){

    Scanner myScanner = new Scanner(System.in);
    String username1;
    String username2;
    int[] scorePlayers = new int[2];
    

    System.out.println("Enter username for Player 1: "); 
    username1 = myScanner.nextLine();  
    System.out.println("Enter username for Player 2: ");
    username2 = myScanner.nextLine();


    System.out.println("Press Enter to start the game!");
    
    System.out.println("Next Player rolls");

    myScanner.close();
 }


    public int throwDie(){
    return (int)(Math.random() * 6) + 1;
}

    public boolean checkWin(int scorePlayer, String username){
       
        if(scorePlayer >= 100)
            return true;
        else
            return false;
    }

    public void playerTurn(int[] scorePlayers, int playerNumber){
         int currentScore = throwDie();
         int unHeldScore = 0; 
         String action;

         if(currentScore == 1)
         {
            playerTurn(scorePlayers, )
         }
         System.out.println("You rolled an " + currentScore + "/n Please type hold or roll to continue.");
         action = myScanner.nextLine();
         while(action.equals("roll") || action.equals("roll")){

         }

    }
    
}
