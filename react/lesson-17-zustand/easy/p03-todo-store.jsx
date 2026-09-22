/*
LESSON 17 — Zustand
EASY P03 — Todo Store
============================================
CONCEPT: Store actions replace a whole reducer+dispatch setup: `addTodo`, `toggleTodo`, `deleteTodo` are just functions in the store that call `set` with the updated array.
PROBLEM: Create `useTodoStore` with `todos: []`, `addTodo(text)` (append `{id: Date.now(), text, done: false}`), `toggleTodo(id)` (map + flip `done`), `deleteTodo(id)` (filter). Build `TodoApp` with a local `useState` input + Add button, and a `<ul>` where each item toggles on click (✓ when done) and has an "x" delete button using `stopPropagation`.
TRY THIS: Render `<TodoApp />`, add two todos, click one to check it, delete the other.
EXPECTED OUTPUT: Todos add, toggle to "✓ text", and delete correctly.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
