import { useState } from 'react'
import './App.css'

function App() {
  
  //overall points for each player
  const [p1Points, setP1Points] = useState(0)
  const [p2Points, setP2Points] = useState(0)

  //Held points for each player
  const[p1Temp, setP1Temp] = useState(0)
  const[p2Temp, setP2Temp] = useState(0)


  //winner message
  const [message, setMessage] = useState('')

  //diable buttons

  const [p1Buttons, setP1Buttons] = useState(false);
  const [p2Buttons, setP2Buttons] = useState(true);


  // dice mechanism random 1-6
  const [rollP1, setRollP1] = useState('')
  
  function rollDiceP1(){
    const max = 6;
    const min = 1
    let value = Math.floor(Math.random() * (max - min + 1) + min);
    if(value ===1){
      //disable P1 buttons
      console.log('P1 rolled a 1')
      setRollP1(0);
      setP1Temp(0);
      return setMessage('Player 1 Turn over! Player 2 go')
    }
    return setRollP1(value), setP1Temp(p1Temp + value)
  }

  const [rollP2, setRollP2] = useState('')
  
  function rollDiceP2(){
    const max = 6;
    const min = 1
    let value = Math.floor(Math.random() * (max - min + 1) + min);
    if(value ===1){
      //disable P1 buttons
      console.log('P1 rolled a 1')
      setRollP2(0);
      setP2Temp(0);
      return setMessage('Player 2 Turn over! Player 1 go')
    }
    return setRollP2(value), setP2Temp(p1Temp + value)
  }

  //update player score
  function holdP1Points(){
    let value = p1Points + p1Temp;
    console.log('P1 hold button pressed')
    //rest roll and temp points values
    setRollP1(0)
    setP1Temp(0)

    return setP1Points(value);
  
  }

  function updateP2(){
    let value = p2Points + p2Temp;
    console.log('P2 hold button pressed')
    //rest roll and temp points values
    setRollP1(0)
    setP1Temp(0)

    return setP2Points(value);
  }

  if(p1Points >= 100){
    setMessage('Player 1 wins!')
    // disable rolling and hold buttons
    //show play again button --> rests the players score to 0
  } else if(p2Points >= 100){
    setMessage('Player 2 wins!')
    // disable rolling and hold buttons
    //show play again button --> rests the players score to 0
  }


  return (
    <div>
      <h2>Dice Game</h2>
      <div className='player-one'>
        <h2>Player 1</h2>
        <p id='player-one-points'>Player 1 Points: {p1Points}</p>

        <button id='roll-dice-P1' onClick={rollDiceP1}>Roll</button>
        <p>Roll value: {rollP1}</p>
        <h2> </h2>

        <p>unheld Score: {p1Temp}</p>
        <button id='hold-points' onClick={holdP1Points}>Hold Points?</button>

      </div>

      <div>
        <h1>{message}</h1>
      </div>

      <div className='player-two'>
        <h2>Player 2</h2>
        <p id='player-two-points'>Player 2 points: {p2Points}</p>

        <button id='roll-dice-P2' onClick={rollDiceP2}>Roll</button>
        <p>Roll value: {rollP2}</p>

        <h2> </h2>

        <p>unheld Score: {p2Temp}</p>
        <button id='hold-points' onClick={updateP2}>Hold Points?</button>

      </div>

    </div>
  )
}

export default App
