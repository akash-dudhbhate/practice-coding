/*
LESSON 05 — Lists & Keys
HARD P03 — Reorderable List with State
============================================
CONCEPT: Reordering is where index keys break — React reuses DOM by key, so key by a stable `item.id` and swap items inside a copied array.
PROBLEM: Build a `ReorderableList` with `items` state (`{id, text}` x3). `move(index, dir)` copies the array, bounds-checks the target, swaps the two elements, and sets state. Each `<li key={item.id}>` shows text plus ↑ / ↓ buttons calling move.
TRY THIS: Render `<ReorderableList />` and press ↓ on "First".
EXPECTED OUTPUT: "First" trades places with "Second"; items keep their identity.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
