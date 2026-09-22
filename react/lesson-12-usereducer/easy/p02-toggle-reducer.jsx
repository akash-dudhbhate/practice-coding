/*
LESSON 12 — useReducer
EASY P02 — Toggle with useReducer
============================================
CONCEPT: Reducers work for booleans too — each action name documents a state transition ("toggle", "on", "off") instead of scattering `setX(!x)` calls around.
PROBLEM: Build a `Toggle` component using `useReducer(reducer, false)` into `isOn`. The reducer switches on the action: `"toggle"` returns `!state`, `"on"` returns true, `"off"` returns false. Render "ON" or "OFF" plus three buttons dispatching each action.
TRY THIS: Render `<Toggle />` and click Toggle twice, then Off.
EXPECTED OUTPUT: Text flips ON → OFF → ON, then Off forces "OFF".
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
