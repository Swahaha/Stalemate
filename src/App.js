import React, { useState, useEffect } from 'react';
import { Chess } from 'chess.js';
import { Chessboard } from "react-chessboard";
import './App.css';

function App() {
  const [game, setGame] = useState(new Chess());

  function makeAMove(move) {
    const gameCopy = new Chess(game.fen());
    let result = null;
    try{
      const result = gameCopy.move(move);
    }
    catch(error){
      console.log("invalid move");
    }
    setGame(gameCopy);
    return result; // null if the move was illegal, the move object if the move was legal
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
    // setTimeout(makeRandomMove, 200);
    return true;
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
