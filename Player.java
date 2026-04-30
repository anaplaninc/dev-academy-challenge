import java.util.*;

public class Player{

    String name;
    List<String> presetNames = new ArrayList<String>(Arrays.asList("Player 1", "Player 2"));

    void Player(Integer playerNumber){
        name = presetNames.get(playerNumber);
    }

    void Player(String name){
        this.name = name;
    }
}