// Developed by Adam Murray
// Controls the game logic
class GameViewModel
{
  late Function _setState;
  set setState(func) => _setState = func;
  final String _player1Name;
  final String _player2Name;
  String get player1Name => _player1Name;
  String get player2Name => _player2Name;

  GameViewModel(this._player1Name, this._player2Name);
}