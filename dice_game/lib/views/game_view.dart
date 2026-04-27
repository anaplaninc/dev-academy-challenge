import 'package:flutter/material.dart';

import '../viewmodels/game_view_model.dart';

// Developed by Adam Murray
// Displays the main game view
class GameView extends StatefulWidget {
  GameView({super.key,
    required String player1Name,
    required String player2Name,
})
{
  _gameViewModel = GameViewModel(player1Name, player2Name);
}

late GameViewModel _gameViewModel;

  @override
  State<GameView> createState() => _GameViewState();
}


class _GameViewState extends State<GameView> {
  late GameViewModel _gameViewModel;

  @override
  void initState() {
    _gameViewModel = widget._gameViewModel;
    _gameViewModel.setState = _setState;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
          children: [
        Row(children: [Text(_gameViewModel.player1Name), Text(_gameViewModel.player2Name)]
        )
          ]
      ),
    );
  }

  _setState() {
    setState(() {});
  }
}
