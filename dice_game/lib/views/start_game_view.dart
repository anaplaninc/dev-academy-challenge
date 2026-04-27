import 'package:dice_game/viewmodels/start_game_viewmodel.dart';
import 'package:flutter/material.dart';

// Developed by Adam Murray
// Displays the pre game settings view
class StartGameView extends StatefulWidget {
  StartGameView({super.key,
    required dynamic Function(String, String) switchToGame,
  })
{
  _startGameViewModel = StartGameViewModel(switchToGame);
}

  late StartGameViewModel _startGameViewModel;

  @override
  State<StartGameView> createState() => _StartGameViewState();
}

class _StartGameViewState extends State<StartGameView> {
  late StartGameViewModel _startGameViewModel;

  @override
  void initState() {
    _startGameViewModel = widget._startGameViewModel;
    _startGameViewModel.setState = _setState;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Row(
            children: [
              Expanded(
                child: TextField(
                  controller: TextEditingController(
                    text: _startGameViewModel.player1Name,
                  ),
                  onChanged: (text) {
                    _startGameViewModel.player1Name = text;
                  },
                  decoration: const InputDecoration(hintText: 'Player 1'),
                ),
              ),
              Expanded(
                child: TextField(
                  controller: TextEditingController(
                    text: _startGameViewModel.player2Name,
                  ),
                  onChanged: (text) {
                    _startGameViewModel.player2Name = text;
                  },
                  decoration: const InputDecoration(hintText: 'Player 2'),
                ),
              ),
            ],
          ),
          ElevatedButton(onPressed: () {_startGameViewModel.switchToGame(_startGameViewModel.player1Name, _startGameViewModel.player2Name);}, child: Text("Start Game")),
        ],
      ),
    );
  }

  _setState() {
    setState(() {});
  }
}
