import { useState } from 'react'
import dice from '../public/dice2.jpg';
import './App.css'
import { roll, type GameState } from './utils'

function App() {

  const initialState: GameState = {
    p1_total: 0,
    p2_total: 0,
    current_player: "p1",
    current_message: "Player 1 turn"
  };

  const [state, setState] = useState<GameState>(initialState);
  const [dice_roll, setDiceRoll] = useState<number>(0);

  function roll_handler() {
    const newRoll = roll();
    setDiceRoll(newRoll);
  }

  function hold() {

    if ((state.p1_total || state.p2_total) >= 100) {
      setState({ ...state, current_message: "Winner!!!!!!!!!" });
      return;
    }

    // todo.. the 1 just end turn thing. 

    if (state.current_player == "p1") {
      setState({ ...state, p1_total: state.p1_total + dice_roll, current_player: "p2", current_message: "Player 2 turn" })
    }
    else {
      setState({ ...state, p2_total: state.p2_total + dice_roll, current_player: "p1", current_message: "Player 1 turn" })
    }
  }

  return (
    <>
      <section id="center">
        <div className="hero">
          <img src={dice} className="base" width="170" height="179" alt="" />
        </div>
        <div>
          <h1>Anaplan Dice Game</h1>
          <p>
            {state.current_message}
          </p>
          <div>
            Scores: Player 1 ({state.p1_total}), Player 2 ({state.p2_total})
          </div>
        </div>

        <button
          type="button"
          className="counter"
          onClick={roll_handler}
        >
          Roll is {dice_roll}
        </button>

        <button onClick={hold}>Hold</button>
      </section>
    </>
  )
}

export default App
