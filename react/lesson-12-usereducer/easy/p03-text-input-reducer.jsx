/*
LESSON 12 — useReducer
EASY P03 — Text Input with Action Payload
============================================
CONCEPT: Actions usually carry data: `{type, payload}`. The reducer reads `action.type` to pick the branch and `action.payload` for the new data — same pattern Redux uses.
PROBLEM: Build a `TextInput` component using `useReducer(reducer, "")`. The reducer returns `action.payload` when `action.type === "SET_TEXT"`, else the state. Render a controlled `<input>` whose `onChange` dispatches `{type: "SET_TEXT", payload: e.target.value}`, plus paragraphs showing the text and its `length`.
TRY THIS: Render `<TextInput />` and type "hello".
EXPECTED OUTPUT: "Text: hello" and "Characters: 5" update as you type.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
