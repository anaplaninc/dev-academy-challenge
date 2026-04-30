import java.util.*;

public class Player{

    String name;
    Integer turnScore = 0;
    Integer totalScore = 0;
    List<String> presetNames = new ArrayList<String>(Arrays.asList("Player 1", "Player 2"));

    public Player(){

    }

    public Player(Integer playerNumber){
        name = presetNames.get(playerNumber-1);
    }

    public Player(String name){
        this.name = name;
    }

    public void bank(Integer heldScore){
        totalScore = heldScore;
    }

    // public void SetTurnScore(Integer turnScore){
    //     this.turnScore = turnScore;
    // }

    // public Integer GetTurnScore(){
    //     return this.turnScore;
    // }
}