package com.example.game.dto;

public class Game {

    private Integer id;
    private String user1;
    private String user2;
    private Player player1;
    private Player player2;


    public Game(Integer id) {
        this.id = id;
        this.user1 = "User1";
        this.user2 = "User2";
        this.player1 = new Player(user1);
        this.player2 = new Player(user2);
    }

    public Game(Integer id, String User1, String User2) {
        this.id = id;
        this.user1 = User1;
        this.user2 = User2;
        this.player1 = new Player(user1);
        this.player2 = new Player(user2);
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUser1() {
        return user1;
    }

    public void setUser1(String user1) {
        this.user1 = user1;
    }

    public String getUser2() {
        return user2;
    }

    public void setUser2(String user2) {
        this.user2 = user2;
    }

    public Player getPlayer1() {
        return player1;
    }

    public void setPlayer1(Player player1) {
        this.player1 = player1;
    }

    public Player getPlayer2() {
        return player2;
    }

    public void setPlayer2(Player player2) {
        this.player2 = player2;
    }
}