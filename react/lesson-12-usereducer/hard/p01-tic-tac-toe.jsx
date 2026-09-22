/*
LESSON 12 — useReducer
HARD P01 — Tic-Tac-Toe Game Reducer
============================================
CONCEPT: Game state is a great reducer fit: every move is one action, and win/draw detection lives inside the pure reducer so the component only renders and dispatches.
PROBLEM: Write `checkWinner(board)` checking the 8 winning lines (return "X"/"O", "draw" when the board is full, else null). Build `TicTacToe` with `useReducer` holding `{board: Array(9).fill(null), currentPlayer: "X", winner: null, isDraw: false}`. On `"MAKE_MOVE"` (payload `action.index`): ignore occupied cells and finished games, copy the board, place `currentPlayer`, run `checkWinner`, flip the player. `"RESET"` restores initial state. Render a status line (winner / draw / whose turn), a 3×3 grid of 9 buttons dispatching MAKE_MOVE, and a Reset button.
TRY THIS: Render `<TicTacToe />` and play X to a top-row win (cells 0,1,2).
EXPECTED OUTPUT: Cells fill alternating X/O; status shows "Winner: X"; Reset clears the board.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
