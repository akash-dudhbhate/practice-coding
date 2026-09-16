/*
LESSON 05 — Lists & Keys
MEDIUM P01 — Dynamic Todo List
============================================
CONCEPT: When items can be added and removed, keys must come from stable ids (like Date.now()) — indexes shift and confuse React.
PROBLEM: Build a `DynamicTodo` component with `todos` and `input` state. Add appends `{ id: Date.now(), text }`; each `<li key={t.id}>` shows the text and an "x" button that filters it out.
TRY THIS: Render `<DynamicTodo />`, add "task one" and "task two", delete the first.
EXPECTED OUTPUT: Items append on Add; clicking x removes only that item.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
