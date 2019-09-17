import React, { Component } from 'react';
import './App.css';
import Row from './Row';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      board: [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]],
      player: "1",
      winner: null,
      message: ""
    };
  }

  initBoard() {
    this.setState({board: [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]],
            player: "1",
            winner: null,
            message: ""
  })};

  play = async (column) => {
    let response = await fetch('/evaluate_board_state', {
      method: 'post',
      body: JSON.stringify({"currentBoard": this.state.board, "player": this.state.player, "column": column}),
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
    });

    let data = await response.json();
    console.log(data)
    this.setState({board: data.board, player: data.player, winner: data.winner, message: data.message});
  };


render() {
   return (
     <div className="game-container">
       <div className="ui button" onClick={() => {this.initBoard()}}>New Game</div>
       <h1> CONNECT FOUR </h1>
       <p><b> Player {this.state.player}'s Move </b></p>
       <p> {this.state.message} </p>
       <table>
         <thead>
         </thead>
         <tbody>
           {this.state.board.map((row, i) => (<Row key={i} row={row} play={this.play} />))}
         </tbody>
       </table>

       <p className="message">{this.state.message}</p>
     </div>
   );
 }
}


export default App;
