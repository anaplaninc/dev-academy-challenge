// Developed by Adam Murray
// Controls the pre game settings logic
class StartGameViewModel
{
  late Function _setState;
  set setState(func) => _setState = func;

  String _player1Name = "Player 1";
  String _player2Name = "Player 2";
  set player1Name(name) => _player1Name = name;
  set player2Name(name) => _player2Name = name;
  String get player1Name => _player1Name;
  String get player2Name => _player2Name;

  late Function(String, String) _switchToGame;
  Function(String,String) get switchToGame => _switchToGame;

  StartGameViewModel(this._switchToGame);

}