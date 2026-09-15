// Lesson 12 — Hard P01: Tic-tac-toe with useReducer
import { useReducer } from "react";
const checkWinner = (board) => {
  const lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
  for (const [a,b,c] of lines) if (board[a] && board[a] === board[b] && board[a] === board[c]) return board[a];
  if (board.every((c) => c)) return "draw";
  return null;
};
const reducer = (state, action) => {
  if (action.type === "MAKE_MOVE") {
    if (state.board[action.index] || state.winner) return state;
    const board = [...state.board];
    board[action.index] = state.currentPlayer;
    const winner = checkWinner(board);
    return { board, currentPlayer: state.currentPlayer === "X" ? "O" : "X", winner, isDraw: winner === "draw" };
  }
  if (action.type === "RESET") return { board: Array(9).fill(null), currentPlayer: "X", winner: null, isDraw: false };
  return state;
};
function TicTacToe() {
  const [state, dispatch] = useReducer(reducer, { board: Array(9).fill(null), currentPlayer: "X", winner: null, isDraw: false });
  return (
    <div>
      <p>{state.winner ? `Winner: ${state.winner}` : state.isDraw ? "Draw!" : `Turn: ${state.currentPlayer}`}</p>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 60px)", gap: "4px" }}>
        {state.board.map((cell, i) => <button key={i} onClick={() => dispatch({ type: "MAKE_MOVE", index: i })} style={{ width: 60, height: 60 }}>{cell}</button>)}
      </div>
      <button onClick={() => dispatch({ type: "RESET" })}>Reset</button>
    </div>
  );
}
export default TicTacToe;
