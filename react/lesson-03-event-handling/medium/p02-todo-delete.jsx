/*
LESSON 03 — Event Handling
MEDIUM P02 — Todo with Delete Buttons
============================================
CONCEPT: Handlers inside `.map()` need the item's id — wrap the call in an arrow function `() => deleteTodo(t.id)` so the argument is passed on click, not on render.
PROBLEM: Build a `TodoDelete` component with `todos` state seeded with two items (`{id, text}`). Each `<li>` renders the text and a Delete button that filters that id out of state.
TRY THIS: Render `<TodoDelete />` and click Delete on the first item.
EXPECTED OUTPUT: The first `<li>` disappears; the other stays.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
