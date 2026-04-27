import 'package:dice_game/viewmodels/view_holder_model.dart';
import 'package:dice_game/views/start_game_view.dart';
import 'package:flutter/material.dart';

// Developed by Adam Murray
// A view that provides the ability to switch between the initial screen and the main game
class ViewHolder extends StatefulWidget
{
  ViewHolder({super.key});

  final ViewHolderModel _viewHolderModel = ViewHolderModel();

  @override
  State<ViewHolder> createState() => _ViewHolderState();

}

class _ViewHolderState extends State<ViewHolder> {

  late ViewHolderModel _viewHolderModel;

  @override
  void initState() {
    _viewHolderModel = widget._viewHolderModel;
    _viewHolderModel.setState = _setState;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(body: _viewHolderModel.currentView);
  }

  _setState()
  {
    setState(() {
    });
  }
}