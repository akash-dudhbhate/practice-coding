# Lesson 02 — State & useState

## What you'll learn
- What state is and why components need it.
- How to use the `useState` hook to add state to function components.
- How to update state correctly (immutable updates for arrays and objects).
- How React batches state updates and why it matters.

## Lesson

State is data that belongs to a component and can change over time. When state changes, React re-renders the component to reflect the new data.

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>Clicked {count} times</button>;
}
```

- `useState(0)` — `0` is the initial value.
- `count` — the current state value.
- `setCount` — the setter function that updates state and triggers re-render.

### Key rules
- **Never mutate state directly.** Always pass a new value to the setter.
- **Arrays/objects:** use spread (`...`) to create copies before updating.
- **Multiple updates in one handler:** use `setCount(prev => prev + 1)` to avoid stale state.
- **Call hooks at the top level** — never inside conditions, loops, or nested functions.
- **Don't store derived values** — compute them during render instead.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.jsx` — **Counter:** A button that increments a count. Display the count inside the button. Start at 0.
2. `easy/p02-solve.jsx` — **Toggle Text:** A button that toggles between showing "ON" and "OFF". Use a boolean state variable.
3. `easy/p03-solve.jsx` — **Text Input Display:** An input field where whatever you type appears below it in real time. Use string state.

### Medium
4. `medium/p01-solve.jsx` — **Todo List Add/Remove:** A todo list where you can add items (input + button) and remove items (click to remove). Use array state with immutable updates.
5. `medium/p02-solve.jsx` — **Counter with Increment/Decrement/Reset:** Three buttons: +1, -1, and Reset. Use functional updates (`prev => prev + 1`). Prevent count from going below 0.
6. `medium/p03-solve.jsx` — **Form with Multiple Fields:** A form with name and email inputs. Display the values below as you type. Use a single object state with spread updates.

### Hard
7. `hard/p01-solve.jsx` — **Shopping Cart:** Add products to a cart, update quantities (+/-), remove items, and show total price. Use array of objects state with immutable updates.
8. `hard/p02-solve.jsx` — **Multi-Step Form:** A 3-step form (name → email → review) with Next/Back buttons. Validate each step before proceeding. Store all data in one state object.
9. `hard/p03-solve.jsx` — **Accordion Component:** A list of sections where clicking one expands it and collapses others (only one open at a time). Track open index in state.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete component from scratch** below the TODO marker.
- Remove the TODO line when done.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
