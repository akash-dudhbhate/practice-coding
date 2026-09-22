/*
LESSON 02 — State & useState
MEDIUM P01 — Todo List Add/Remove
============================================
CONCEPT: Array state must be updated immutably: add with spread `[...todos, item]` and remove with `.filter()` — never push/splice the old array.
PROBLEM: Build a `TodoList` component. Keep `todos` (array) and `input` (string) state. An input + Add button appends `{ id: Date.now(), text }`; clicking a rendered `<li>` removes it via `filter`. Render items with `.map()` and `key={t.id}`.
TRY THIS: Render `<TodoList />`, type "Buy milk", click Add, then click the item to remove it.
EXPECTED OUTPUT: Typing + Add appends an `<li>`; clicking the `<li>` deletes it.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
