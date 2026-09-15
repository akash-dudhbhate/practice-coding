# Lesson 08 — Coding Check

## Easy

### p01-solve.jsx — Auto-focus on mount
- [ ] Input element exists
- [ ] `useRef` creates a ref for the input
- [ ] `useEffect` focuses the input on mount
- [ ] Empty dependency array `[]` (runs once)
- [ ] Input is focused when component loads

### p02-solve.jsx — Focus on button click
- [ ] Input and button exist
- [ ] `useRef` attached to input
- [ ] Button click calls `inputRef.current.focus()`
- [ ] Input gets focus when button is clicked

### p03-solve.jsx — Click counter with ref
- [ ] `useRef(0)` for count
- [ ] Button increments `ref.current`
- [ ] `console.log` shows the incrementing value
- [ ] Displayed count does NOT update (demonstrating ref vs state)
- [ ] Comment explains why display doesn't update

## Medium

### p01-solve.jsx — Stopwatch
- [ ] Start button begins the timer
- [ ] Stop button pauses the timer
- [ ] Reset button sets time to 0
- [ ] `useRef` stores the interval ID
- [ ] `useState` stores the displayed time
- [ ] Cleanup clears interval on unmount

### p02-solve.jsx — usePrevious hook
- [ ] `usePrevious(value)` custom hook defined
- [ ] Uses `useRef` and `useEffect`
- [ ] Returns the previous value
- [ ] Component displays "Current: X, Previous: Y"
- [ ] Previous value updates correctly when state changes

### p03-solve.jsx — CustomInput with forwardRef
- [ ] `CustomInput` uses `forwardRef`
- [ ] Ref is attached to the inner `<input>`
- [ ] Parent creates a ref and passes it to `CustomInput`
- [ ] Parent can call `inputRef.current.focus()`
- [ ] Focus works on the child input

## Hard

### p01-solve.jsx — VideoPlayer
- [ ] `<video>` element with `useRef`
- [ ] Play button calls `videoRef.current.play()`
- [ ] Pause button calls `videoRef.current.pause()`
- [ ] Seek functionality (jump to time)
- [ ] Displays current time / duration
- [ ] Controls are responsive

### p02-solve.jsx — ScrollToTop button
- [ ] Button appears after scrolling 200px
- [ ] `useState` tracks visibility
- [ ] Scroll event listener added in `useEffect`
- [ ] Clicking button scrolls to top (`window.scrollTo`)
- [ ] Smooth scroll behavior
- [ ] Listener cleaned up on unmount

### hard/p03-solve.jsx — CustomForm with useImperativeHandle
- [ ] `CustomForm` uses `forwardRef` and `useImperativeHandle`
- [ ] Exposes `focus()` method
- [ ] Exposes `clear()` method
- [ ] Exposes `validate()` method (checks required fields)
- [ ] Exposes `submit()` method
- [ ] Parent calls these methods via ref
- [ ] Parent doesn't have direct DOM access (encapsulated)
