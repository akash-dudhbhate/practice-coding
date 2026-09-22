/*
LESSON 11 — Context API
HARD P01 — Shopping Cart: Context + useReducer
============================================
CONCEPT: When context state has many update shapes (add/remove/update/clear), pairing it with useReducer keeps the logic in one pure reducer while context handles distribution. Consumers just call `dispatch`.
PROBLEM: Create `CartContext` and a `cartReducer` handling action types `"ADD_ITEM"` (increment `qty` if the item id already exists), `"REMOVE_ITEM"`, `"UPDATE_QTY"`, and `"CLEAR"`. Export a `CartProvider({children})` that runs `useReducer(cartReducer, {items: [], total: 0})`, computes `total` with `reduce` over `price * qty`, and provides `{...state, total, dispatch}`. Export a `useCart()` hook that throws if used outside the provider.
TRY THIS: Wrap an app in `<CartProvider>` and call `useCart().dispatch({type:"ADD_ITEM", item:{id:1, price:10}})` from a button.
EXPECTED OUTPUT: Items accumulate with quantities; `total` reflects price × qty; CLEAR empties the cart.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
