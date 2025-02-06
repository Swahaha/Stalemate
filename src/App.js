import React, { useState, useEffect } from 'react';
import { Chess } from 'chess.js';
import { Chessboard } from "react-chessboard";
import './App.css';

function App() {
  const [game, setGame] = useState(new Chess());

  function makeAMove(move) {
    const gameCopy = new Chess(game.fen());
    let result = null;
    try {
      result = gameCopy.move(move);
    } catch (error) {
      console.log("Invalid move");
    }
    if (result) {
      setGame(gameCopy);
    }
    return result;
  }

  // function makeRandomMove() {
  //   const possibleMoves = game.moves();
  //   if (game.game_over() || game.in_draw() || possibleMoves.length === 0)
  //     return; // exit if the game is over
  //   const randomIndex = Math.floor(Math.random() * possibleMoves.length);
  //   makeAMove(possibleMoves[randomIndex]);
  // }

  function onDrop(sourceSquare, targetSquare) {
    const move = makeAMove({
      from: sourceSquare,
      to: targetSquare,
      promotion: "q", // always promote to a queen for example simplicity
    });

    // illegal move
    if (move === null) return false;

    setTimeout(getBestMove, 500);
    // setTimeout(makeRandomMove, 200);
    return true;
  }

  function getBestMove() {
    const fen = game.fen(); 
    console.log("hello")
    fetch('http://127.0.0.1:5000/get_best_move', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ fen: fen })
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.best_move)
      if (data.best_move) {
        makeAMove({ from: data.best_move.slice(0, 2), to: data.best_move.slice(2, 4) });
      } else {
        console.error("Error:", data.error);
      }
    })
    .catch(error => console.error("Fetch error:", error));
  }


  return (
    <div className="App">
      <header className="App-header">
        <div>
          <Chessboard 
          id="BasicBoard" 
          boardWidth={500} 
          position={game.fen()} 
          onPieceDrop={onDrop} 
          animationDuration={0}/>
        </div>
      </header>
    </div>
  );
}

export default App;
