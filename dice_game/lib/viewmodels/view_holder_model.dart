import 'package:dice_game/views/game_view.dart';
import 'package:dice_game/views/start_game_view.dart';
import 'package:flutter/material.dart';

// Developed by Adam Murray
// Controls the view holder logic
class ViewHolderModel {

  late Function _setState;
  set setState(func) => _setState = func;
  late Widget currentView;

  ViewHolderModel()
  {
    currentView = StartGameView(switchToGame: switchToGameView);
  }

  switchToGameView(String player1Name, String player2Name)
  {
    currentView = GameView(player1Name: player1Name, player2Name: player2Name);
    _setState();
  }

}