package org.example;

public class Game {
    private boolean is_active = false; // Track whether game has finished
    private boolean turn = true; // True for 1, False for 2

    public boolean get_turn(){
        return turn;
    }

    public void set_turn() {
        turn = !turn;
    }

    // Check whether game is active
    public boolean get_game() {
        return is_active;
    }


    public void end_game() {
        is_active = false;
    }

    // Generate an int between 1 and 6
    public int roll() {
        return (int) (Math.random() * (6-1) + 1);
    }

    public int hold(int score, int roll) {
        return score + roll;
    }

}

