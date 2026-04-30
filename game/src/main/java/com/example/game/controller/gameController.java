package com.example.game.controller;

import com.example.game.dto.Game;
import com.example.game.dto.Player;
import com.example.game.service.GameService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController    //used to identify this class as a rest controller
@RequestMapping("/tasks") //the url path for this controller
public class gameController {

    private final GameService gameService;
    private final Game game = new Game(1);

    public gameController(GameService gameService) {
        this.gameService = gameService;
    }

    @GetMapping  //used for get requests
    public ResponseEntity<Player> getPlayer(@PathVariable String username)
    {
        return ResponseEntity.ok(gameService.getPlayer(username));
    }

    @GetMapping
    public ResponseEntity<Player> rollDice(@PathVariable String username) {
        return ResponseEntity.ok(gameService.rollDice(username));
    }

}