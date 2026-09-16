/*
LESSON 12 — useReducer
MEDIUM P03 — Todos: useReducer + Context
============================================
CONCEPT: useReducer + Context is the classic "mini Redux": the reducer owns all state transitions, the Provider distributes `{state, dispatch}` to the whole tree.
PROBLEM: Create `TodoContext` and a todo reducer handling `"ADD"` (append `{id, text, done: false}`), `"TOGGLE"` (flip `done` by id), `"DELETE"` (filter by id), `"CLEAR_COMPLETED"` (drop done items). Build `TodoProvider({children})` running `useReducer` and providing `{todos, dispatch}`. Build `TodoApp` that consumes the context: an Add button, a `<ul>` of todos (click an item to TOGGLE, show ✓ when done), and a stats line with total and done counts.
TRY THIS: Render `<TodoApp />`, click Add twice, click one item.
EXPECTED OUTPUT: Two items; the clicked one shows "✓"; stats read "Total: 2, Done: 1".
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
