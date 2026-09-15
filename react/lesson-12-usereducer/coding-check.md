# Lesson 12 — Coding Check

## Easy

### p01-solve.jsx — Counter reducer
- [ ] Reducer function handles increment, decrement, reset
- [ ] `default: return state` present
- [ ] `useReducer` used (not useState)
- [ ] Count displayed
- [ ] Buttons dispatch correct actions

### p02-solve.jsx — Toggle reducer
- [ ] Actions: toggle, on, off
- [ ] `toggle` flips the boolean
- [ ] `on` sets to true, `off` sets to false
- [ ] State and buttons displayed
- [ ] Reducer is a pure function

### p03-solve.jsx — Text input reducer
- [ ] Action `SET_TEXT` with payload
- [ ] Reducer updates text from payload
- [ ] Text displayed
- [ ] Character count displayed
- [ ] Input updates the state via dispatch

## Medium

### p01-solve.jsx — Shopping cart reducer
- [ ] ADD_ITEM adds item to cart
- [ ] REMOVE_ITEM removes by id
- [ ] UPDATE_QTY changes item quantity
- [ ] CLEAR empties the cart
- [ ] Total price calculated correctly
- [ ] All state updates are immutable (spread operator)

### p02-solve.jsx — Multi-step form reducer
- [ ] State has step, formData, errors
- [ ] NEXT_STEP increments step
- [ ] PREV_STEP decrements step
- [ ] UPDATE_FIELD updates form data
- [ ] SET_ERROR sets error for a field
- [ ] Current step and relevant fields displayed
- [ ] Step navigation works

### p03-solve.jsx — Todo with Context + reducer
- [ ] TodoProvider uses useReducer
- [ ] Actions: ADD, TOGGLE, DELETE, CLEAR_COMPLETED
- [ ] Context provides state and dispatch
- [ ] Add form component consumes context
- [ ] Todo list component consumes context
- [ ] Stats component shows counts
- [ ] No prop drilling

## Hard

### p01-solve.jsx — Tic-tac-toe reducer
- [ ] Board is array of 9 cells (null, "X", or "O")
- [ ] MAKE_MOVE places current player's mark
- [ ] Switches player after each move
- [ ] Detects winner (3 in a row)
- [ ] Detects draw (board full, no winner)
- [ ] RESET clears the board
- [ ] Can't overwrite a filled cell
- [ ] Game stops when winner is found

### p02-solve.jsx — Data fetching reducer
- [ ] State: {data, loading, error}
- [ ] FETCH_START sets loading=true
- [ ] FETCH_SUCCESS sets data, loading=false
- [ ] FETCH_ERROR sets error, loading=false
- [ ] RESET clears all state
- [ ] Race condition handled (latest request wins)
- [ ] `useFetchReducer` hook encapsulates logic
- [ ] Cleanup on unmount

### p03-solve.jsx — App state with combined reducer
- [ ] Root state has auth, theme, notifications sub-states
- [ ] Auth: LOGIN, LOGOUT actions
- [ ] Theme: TOGGLE_THEME action
- [ ] Notifications: ADD_NOTIFICATION, REMOVE_NOTIFICATION
- [ ] All via Context + useReducer
- [ ] Different components consume different parts
- [ ] Actions are namespaced or clearly separated
- [ ] No prop drilling
