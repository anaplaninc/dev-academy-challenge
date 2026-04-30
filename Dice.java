import java.util.*;

public class Dice {
    // List<Integer> values = new ArrayList<>(Arrays.asList(1,2,3,4,5,6)); 
    Integer currentValue;

    void Dice(){
    }

    static Integer Roll(){
        Random random = new Random();
        Integer value = random.nextInt(6);
        System.out.println("You rolled a " + value);
        return value;
    }

}
