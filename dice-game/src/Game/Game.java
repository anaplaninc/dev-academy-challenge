package Game;

import Model.Dice;
import Model.Player;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Game {

    List<Player> players;
    private int target;
    private Dice dice;
    private int activePlayerIndex;
    Scanner scanner;

    public Game() {
        this.target = 100;
        this.dice = new Dice(6);
        players = new ArrayList<>();
        createPlayers();
        this.activePlayerIndex = 0;
        this.scanner = new Scanner(System.in);
        play();
    }

    public void play() {
        // while true loop that
        while (true) {
            int active = 0;
            takeTurn(active);

            if (players.get(activePlayerIndex).getHeld() > target) {
                win();
                break;
            }

            //Switch the active player.
            if (active == 0) {
                active = 1;
            } else {
                active = 0;
            }
        }
    }



    public boolean takeTurn(int activePlayerIndex) {
        Player activePlayer = players.get(activePlayerIndex);
        System.out.println("Current score: " + activePlayer.getHeld());
        int currentRoundScore = 0;
        String choice = "";

        while (true) {
            System.out.println(activePlayer.getName());
            System.out.println("Roll the dice? (yes/no)");
            choice = scanner.next().toLowerCase();

            if (choice.equals("yes")) {
                int roll = dice.roll();
                if (roll == 1) {
                    // Failure condition
                    // Including switching activePlayerIndex between 0/1
                    //No need to reset "unheld" as that's held in the Game object and will be initialised as 0 next turn
                } else {
                    currentRoundScore += roll;
                    System.out.println("Your round score is " + currentRoundScore);
                    int potentialTotalScore = activePlayer.getHeld() + currentRoundScore;
                    if (potentialTotalScore >= target) {
                        System.out.println("Congratulations. You have won with a total score of " + potentialTotalScore);
                        System.out.println(activePlayer.getName() + " has won");
                        return true;
                    }

                    System.out.println("If banked, your total score would " + potentialTotalScore);
                    continue;
                }
            } else if (choice.equals("no")) {
                activePlayer.bank(currentRoundScore);
                System.out.println("Round over. your total score is " + activePlayer.getHeld());
            } else {
                System.out.println("Invalid choice.");
                continue;
            }



        }
    }

    public void win() {
        Player activePlayer = players.get(activePlayerIndex);
        System.out.println("Congratulation " + activePlayer.getName() + " you have won with a score of " + activePlayer.getHeld());
    }






    public void createPlayers() {
        System.out.println("Player 1, what is your name? (Leave blank for default");
        String playerOneName = scanner.next();
        players.add(createPlayer(playerOneName, 1));
        System.out.println("Player 2, what is your name? (Leave blank for default");
        String playerTwoName = scanner.next();
        players.add(createPlayer(playerTwoName, 2));

    }

    public Player createPlayer(String name, int playerNumber) {
        return new Player(name, playerNumber);
    }



}
