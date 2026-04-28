package org.example;

import java.util.Scanner;

public class Player {
    private String player_name;
    private int score = 0;
    private Game game;

    public Player(String name, Game created_game) {
        player_name = name; // Allow for predefined name
        game = created_game;
    }

    public int get_score() {
        return score;
    }

    public void set_score(int new_score) {
        score = new_score;
    }

    // Essentially the player's turn
    public void do_action() {
        // Roll dice
        int roll = game.roll();

        // Show to user

        // We will put a scanner here for now (unsure)
        Scanner scan = new Scanner(System.in);
        String roll_str = "Rolled a %d. What action would you like to take? (H / D)";
        System.out.println(String.format(roll_str, roll));

        // Get input
        String input = scan.nextLine();
        if(input.equals("H")) {
            int new_score = game.hold(get_score(), roll);
            set_score(new_score);
        }
        else if(input.equals("D")) {
            do_action(); // TODO: Need to check this is right
        }
        else {
            // invalid input - TODO: loop until it is valid
        }

        // End turn
        game.set_turn();

        // End game if applicable
        if(score >= 100) {
            game.end_game();
        }


    }
}
