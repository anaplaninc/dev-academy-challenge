package com.example.game.dto;

public class Player {

    private String username;
    private Integer savedScore;
    private Integer unsavedScore;

    public Player(String username) {
        this.username = username;
        this.savedScore = 0;
        this.unsavedScore = 0;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public Integer getSavedScore() {
        return savedScore;
    }

    public void setSavedScore(Integer savedScore) {
        this.savedScore = savedScore;
    }

    public Integer getUnsavedScore() {
        return unsavedScore;
    }

    public void setUnsavedScore(Integer unsavedScore) {
        this.unsavedScore = unsavedScore;
    }
}
