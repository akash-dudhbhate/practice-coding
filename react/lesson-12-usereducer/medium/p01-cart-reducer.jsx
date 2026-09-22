/*
LESSON 12 — useReducer
MEDIUM P01 — Shopping Cart Reducer
============================================
CONCEPT: Array state with several update shapes is where useReducer shines: each action type is one named transformation, all in one testable pure function.
PROBLEM: Build a `Cart` component using `useReducer(reducer, [])` for `items`. The reducer switches on `action.type`: `"ADD_ITEM"` (payload `action.item`; bump `qty` if the id already exists, else append with `qty: 1`), `"REMOVE_ITEM"` (filter by `action.id`), `"UPDATE_QTY"` (map, set `qty` to `action.qty`), `"CLEAR"` (empty array). Compute `total` with `reduce` over `price * qty`. Render an Add button, the item list (with `key`), and the total.
TRY THIS: Render `<Cart />` and click "Add Apple" three times.
EXPECTED OUTPUT: One line "Apple x3 = $3" and "Total: $3" — duplicates merge via qty.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
