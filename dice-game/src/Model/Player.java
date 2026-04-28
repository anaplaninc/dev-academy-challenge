package Model;

public class Player {

    // Requires:
    // Name with default set to player 1, player 2
    // held score
    // Unheld score
    private String name;
    private int held;

    public Player(String name, int playerNumber) {
        if (name.isBlank()) {
            this.name = "Player " + playerNumber;
        } else {
            this.name = name;
        }
        this.held = 0;
    }

    public void bank(int unheld) {
        this.held += unheld;
    }

    public int getHeld() {
        return this.held;
    }

    public void setHeld(int newHeld) {
        this.held = newHeld;
    }

    public String getName(){
        return this.name;
    }


}
