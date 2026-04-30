package com.example.game.service;

import com.example.game.dto.Game;
import com.example.game.dto.Player;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class GameService {

    public GameService() {}

    public Game startGame(Integer id, String user1, String user2){
        return new Game(id, user1, user2);
    }

    public Player getPlayer(String name) {
        //returns the player stats including their saved and unsaved score
        return null;
    }



}
