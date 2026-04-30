import java.util.*;

public class Dice {

    void Dice(){
    }

    // Roll a random number between 1 and 6
    static Integer Roll(){
        Random random = new Random();
        Integer value = random.nextInt(6);
        System.out.println("You rolled a " + value);
        return value;
    }

}
