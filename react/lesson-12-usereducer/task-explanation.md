# Lesson 12 — useReducer

## What you'll learn
- useReducer basics (reducer function, actions, dispatch)
- useState vs useReducer (when to use which)
- Action types and payloads
- Complex reducer patterns (forms, carts)
- useReducer with Context (global state)
- Lazy initialization
- Testing reducers (pure functions)

## Lesson

### Basic reducer
```jsx
function reducer(state, action) {
    switch (action.type) {
        case 'increment': return { ...state, count: state.count + 1 };
        default: return state;
    }
}
const [state, dispatch] = useReducer(reducer, { count: 0 });
```

### With payload
```jsx
dispatch({ type: 'set_name', payload: "Akash" });
case 'set_name': return { ...state, name: action.payload };
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create a counter with `useReducer`: actions for increment, decrement, and reset. Display the count and buttons.
2. `easy/p02-solve.jsx` — Create a toggle component with `useReducer`: actions for `toggle`, `on`, and `off`. Display the state and buttons.
3. `easy/p03-solve.jsx` — Create a text input component with `useReducer`: action `SET_TEXT` with payload. Display the current text and character count.

### Medium
4. `medium/p01-solve.jsx` — Create a shopping cart reducer: actions ADD_ITEM (with item payload), REMOVE_ITEM (with id payload), UPDATE_QTY (with id and qty payload), CLEAR. Display cart items and total.
5. `medium/p02-solve.jsx` — Create a multi-step form with `useReducer`: state has `step`, `formData`, `errors`. Actions: NEXT_STEP, PREV_STEP, UPDATE_FIELD, SET_ERROR. Display the current step and form fields.
6. `medium/p03-solve.jsx` — Combine `useReducer` with Context: create a `TodoProvider` with a todo reducer (ADD, TOGGLE, DELETE, CLEAR_COMPLETED). Multiple components consume it (add form, todo list, stats).

### Hard
7. `hard/p01-solve.jsx` — Build a game state reducer (tic-tac-toe): state has `board` (9 cells), `currentPlayer`, `winner`, `isDraw`. Actions: MAKE_MOVE (with index), RESET. Display the board, handle win/draw detection in the reducer.
8. `hard/p02-solve.jsx` — Build a data fetching reducer: state has `{data, loading, error}`. Actions: FETCH_START, FETCH_SUCCESS, FETCH_ERROR, RESET. Create a `useFetchReducer` hook. Handle race conditions (latest request wins).
9. `hard/p03-solve.jsx` — Build a complete app state with `useReducer` + Context: auth (login/logout), theme (toggle), notifications (add/remove). One root reducer with combined sub-states. Multiple components consume different parts.

### How to work
- Write your complete React solution (reducer, component).
- Remove the TODO comment when done.
- Test by importing into a React app or using a sandbox.
