# Lesson 10 — Coding Check

## Easy

### p01-solve.jsx — useToggle
- [ ] Hook returns `{value, toggle, setTrue, setFalse}`
- [ ] `toggle()` flips the boolean
- [ ] `setTrue()` and `setFalse()` set specific values
- [ ] Used in a component to show/hide text
- [ ] Hook name starts with `use`

### p02-solve.jsx — useCounter
- [ ] Hook returns `{count, increment, decrement, reset}`
- [ ] `increment()` increases by 1
- [ ] `decrement()` decreases by 1
- [ ] `reset()` sets count to 0
- [ ] Component displays count with buttons

### p03-solve.jsx — useWindowSize
- [ ] Hook returns `{width, height}`
- [ ] Initial values from `window.innerWidth/innerHeight`
- [ ] Updates on resize event
- [ ] Event listener cleaned up on unmount
- [ ] Component displays current window size

## Medium

### p01-solve.jsx — useFetch
- [ ] Hook takes URL, returns `{data, loading, error}`
- [ ] `loading` is true initially, false after fetch
- [ ] `error` is set on fetch failure
- [ ] `data` is set on success
- [ ] Cleanup prevents state update after unmount (cancelled flag)
- [ ] Fetches from a real API (e.g., JSONPlaceholder)

### p02-solve.jsx — useLocalStorage
- [ ] Hook takes `key` and `initialValue`
- [ ] Reads from localStorage on init
- [ ] Writes to localStorage on value change
- [ ] Theme persists across page reload
- [ ] Username persists across page reload
- [ ] Handles JSON parse errors gracefully

### p03-solve.jsx — useDebounce
- [ ] Hook takes `value` and `delay`
- [ ] Returns debounced value
- [ ] Debounced value updates only after delay
- [ ] Timer cleared on value change (no stale updates)
- [ ] Search only triggers 500ms after last keystroke

## Hard

### p01-solve.jsx — useEventListener
- [ ] Hook takes `eventName`, `handler`, `element`
- [ ] Handler saved in ref (always latest)
- [ ] Listener added on mount
- [ ] Listener removed on unmount
- [ ] Escape key closes modal
- [ ] Click outside closes dropdown
- [ ] Scroll position tracked

### p02-solve.jsx — useForm
- [ ] Hook takes initial values and validate function
- [ ] Returns `{values, errors, handleChange, handleSubmit}`
- [ ] `handleChange` updates field values
- [ ] `handleSubmit` validates and calls callback
- [ ] Validation errors displayed
- [ ] Registration form with 4 fields works correctly
- [ ] Password match validation works

### p03-solve.jsx — Composed hooks
- [ ] `useUserDashboard` uses `useFetch`, `useDebounce`, `useLocalStorage`
- [ ] Fetches user data on mount
- [ ] Search is debounced
- [ ] Preferences saved to localStorage
- [ ] Dashboard displays user info, search results, and preferences
- [ ] All hooks work together without conflicts
