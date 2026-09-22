/*
LESSON 12 — useReducer
EASY P01 — Counter with useReducer
============================================
CONCEPT: useReducer moves update logic out of the component into a pure `reducer(state, action)` function. Instead of calling a setter with a new value, you `dispatch` an action describing WHAT happened.
PROBLEM: Build a `Counter` component using `useReducer(reducer, 0)`. The reducer is a switch on the action handling `"increment"` (state + 1), `"decrement"` (state - 1), and `"reset"` (0). Render the count in a paragraph and three buttons dispatching each action.
TRY THIS: Render `<Counter />` and click +1 twice, then Reset.
EXPECTED OUTPUT: "Count: 2" after two clicks; "Count: 0" after Reset.
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
