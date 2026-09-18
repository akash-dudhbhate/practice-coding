# Lesson 08 — useRef & DOM Access

## What you'll learn
- useRef basics (mutable, no re-render)
- Accessing DOM elements (focus, scroll, measure)
- useRef for timers (setInterval, cleanup)
- Tracking previous values
- useRef vs useState (when to use which)
- forwardRef (passing refs to child components)
- Measuring elements with getBoundingClientRect
- useImperativeHandle (controlled ref API)

## Lesson

### DOM access
```jsx
const inputRef = useRef(null);
<input ref={inputRef} />
<button onClick={() => inputRef.current.focus()}>Focus</button>
```

### Timer with cleanup
```jsx
const timerRef = useRef(null);
useEffect(() => () => clearInterval(timerRef.current), []);
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create a component with an input that auto-focuses on mount using `useRef` and `useEffect`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | |                    |   <- cursor already blinking inside
   +----------------------+      the input on page load
   ```
2. `easy/p02-solve.jsx` — Create a component with a button that focuses a text input when clicked.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   |                      |   <- focus jumps here on click
   +----------------------+
   [ Focus the input ]
   ```
3. `easy/p03-solve.jsx` — Create a component that tracks how many times a button is clicked using `useRef` (NOT state). Display the count — note that it won't update visually (demonstrate ref vs state).

   WHAT IT SHOULD LOOK LIKE:
   ```
   PAGE (stays stale!):     CONSOLE:
   Clicks: 0                1
   [ Click me ]             2
                            3      <- ref changes but no re-render
   ```

### Medium
4. `medium/p01-solve.jsx` — Create a `Stopwatch` component with Start, Stop, and Reset buttons. Use `useRef` for the interval ID and `useState` for the displayed time.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Time: 3.4s                        <- <p> ticks up
   +-------+ +------+ +-------+
   | Start | | Stop | | Reset |
   +-------+ +------+ +-------+
   ```
5. `medium/p02-solve.jsx` — Create a `usePrevious` custom hook that returns the previous value of any state or prop. Use it in a component to show "Current: X, Previous: Y".

   WHAT IT SHOULD LOOK LIKE:
   ```
   Current: 2, Previous: 1           <- <p> always one step behind
   [ Increment ]
   ```
6. `medium/p03-solve.jsx` — Create a `CustomInput` component using `forwardRef`. The parent should be able to focus the input via a ref.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | styled input         |   <- <CustomInput>, focus lands
   +----------------------+      inside on button click
   [ Focus ]
   ```

### Hard
7. `hard/p01-solve.jsx` — Build a `VideoPlayer` component with play/pause/seek controls using `useRef` to access the `<video>` element. No external libraries.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +--------------------------------+
   |          VIDEO                 |   <- <video> element
   |          00:12                 |
   +--------------------------------+
   [ Play/Pause ] [ Restart ] [ +10s ]
   ```
8. `hard/p02-solve.jsx` — Build a `ScrollToTop` button that appears after scrolling down 200px. Use `useRef` for scroll listener cleanup and `useState` for visibility.

   WHAT IT SHOULD LOOK LIKE:
   ```
   . long page content .
   .                   .
   .                   .        +--------+
   .                   .        | ^ Top  |  <- fixed button, bottom
                               +--------+    right, appears after 200px
   ```
9. `hard/p03-solve.jsx` — Build a `CustomForm` component using `forwardRef` + `useImperativeHandle`. Expose `focus()`, `clear()`, `validate()`, and `submit()` methods to the parent. Parent calls these via ref.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | field value          |   <- <CustomForm> (child)
   +----------------------+
   [Focus] [Clear] [Validate] [Submit]  <- parent buttons drive
                                          the child via ref methods
   ```

### How to work
- Write your complete React component solution.
- Remove the TODO comment when done.
- Test by importing into a React app or using a sandbox.
