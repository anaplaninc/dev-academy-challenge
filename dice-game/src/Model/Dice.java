package Model;

import java.util.Random;

public class Dice {

    // This will allow us instantiate a dice with a different number of sides
        // Default 6
    private int sides;

    public Dice(int sides) {
        this.sides = sides;
    }

    public int roll() {
        Random random = new Random();
        int roll = random.nextInt(6) + 1;
        System.out.println("You rolled " + roll);
        return roll;
    }
}
