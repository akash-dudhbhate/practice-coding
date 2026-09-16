/*
LESSON 05 — Lists & Keys
HARD P02 — Todo List with Item Components
============================================
CONCEPT: Extracting a row into its own component keeps lists readable. The `key` goes on the `<TodoItem>` in the parent's map — not inside the child.
PROBLEM: Build a `TodoItem({ todo, onDelete })` component rendering `<li>` with text + Delete button, then a `TodoWithComponents` component holding `todos` state that maps each todo to `<TodoItem key={t.id} todo={t} onDelete={remove} />`. Export `TodoWithComponents` as default.
TRY THIS: Render `<TodoWithComponents />` and delete an item.
EXPECTED OUTPUT: Two todos render; Delete removes the clicked one.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
