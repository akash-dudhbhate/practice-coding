# Lesson 02 — Concepts Explained (State & useState)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## State in React

**What:** State is data that belongs to a component and can change over time. When state changes, React re-renders the component to show the new data.

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);  // state variable + setter
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

- `count` is the current value (starts at 0).
- `setCount` is the function that updates it.
- When `setCount` is called, React re-renders the component with the new value.

**Why it exists:** Props are read-only — a component can't change its own props. Without state, components would be static. State lets components manage their own data that changes over time (user input, toggles, counters, form data).

**Where it's used:** Everywhere interactive — counters, toggles, form inputs, modals (open/closed), tabs, theme (dark/light), shopping carts, anything that changes.

**What goes wrong without it:**
- Using a regular variable: `let count = 0; count++` → the value changes but React doesn't re-render, so the UI never updates. You click and nothing happens.
- Trying to mutate props to "change" data → React doesn't detect the change, UI stays stale.
- No way to build interactive components — everything is frozen.

---

## useState Hook

**What:** `useState` is a React hook that adds state to a function component. It returns an array with two items: the current state value and a setter function.

```jsx
const [state, setState] = useState(initialValue);

// Example: text state
function TextInput() {
  const [text, setText] = useState("");
  return <input value={text} onChange={(e) => setText(e.target.value)} />;
}
```

- `initialValue` is the starting value (can be string, number, boolean, array, object, null).
- You can call `useState` multiple times for multiple state variables.
- The setter function (`setText`) triggers a re-render when called.

**Why it exists:** Before hooks (React 16.8), only class components could have state. `useState` brings state to function components, which are simpler and easier to reason about.

**Where it's used:** Every function component that needs to track changing data.

**What goes wrong without it:**
- Calling `useState` conditionally (inside an `if`) → React relies on call order. If you skip a hook call, the order shifts and state gets assigned to the wrong variable.
- Using the state variable directly to update: `count = count + 1` → doesn't trigger re-render, React doesn't know it changed.
- Destructuring wrong: `const state = useState(0)` → `state` is the array `[0, f]`, not the value. Must destructure: `const [count, setCount] = useState(0)`.

---

## State Updates with Setter Function

**What:** You update state by calling the setter function. You can pass a new value or a function that computes the new value from the old one.

```jsx
const [count, setCount] = useState(0);

// Direct value
setCount(5);

// Based on previous value (functional update)
setCount(count + 1);          // works, but can be stale
setCount(prev => prev + 1);   // safer: always uses latest value
```

The functional update form `setCount(prev => prev + 1)` is safer when multiple updates happen in the same render cycle.

**Why it exists:** React batches state updates for performance. If you call `setCount(count + 1)` three times in a row, they all use the SAME `count` value (stale), so only +1 happens. The functional form `prev => prev + 1` always gets the latest value, so three calls give +3.

**Where it's used:** Counters, increment/decrement buttons, toggling booleans, adding items to arrays, any update that depends on the previous value.

**What goes wrong without it:**
- `setCount(count + 1)` called 3 times in a loop → only increments by 1 (all use same stale `count`).
- Mutating state directly: `count++` or `state.items.push(newItem)` → React doesn't detect the change, no re-render.
- Forgetting to call the setter: `count = 5` → React never knows, UI stays at old value.

---

## Immutable State Updates

**What:** You must NEVER mutate state directly. Always create a new copy (new array, new object) and pass it to the setter. React compares references — if the reference is the same, it skips re-rendering.

```jsx
const [items, setItems] = useState([1, 2, 3]);

// WRONG — mutates the original array
items.push(4);
setItems(items);  // React sees same reference → no re-render

// RIGHT — creates a new array
setItems([...items, 4]);         // spread + new item
setItems(items.filter(i => i !== 2));  // new array without 2
setItems(items.map(i => i * 2));       // new array with doubled values

// For objects:
const [user, setUser] = useState({ name: "Akash", age: 25 });
// RIGHT — spread to create new object
setUser({ ...user, age: 26 });
```

**Why it exists:** React uses shallow comparison (reference equality) to decide if state changed. If you mutate the same object/array, the reference is identical — React thinks nothing changed and skips the re-render. Creating a new copy gives a new reference, so React knows it changed.

**Where it's used:** Every state update involving arrays or objects — todo lists, form data, user profiles, cart items, nested data.

**What goes wrong without it:**
- `items.push(4); setItems(items)` → same array reference → React skips re-render → UI doesn't update.
- `user.age = 26; setUser(user)` → same object reference → no re-render.
- Mutating nested objects: `setUser({ ...user })` but then `user.address.city = "NYC"` inside → nested mutation not detected. Must spread deeply: `setUser({ ...user, address: { ...user.address, city: "NYC" } })`.

---

## Multiple State Variables

**What:** A component can have multiple `useState` calls, each managing a different piece of state.

```jsx
function ContactForm() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [errors, setErrors] = useState({});

  return (
    <form>
      <input value={name} onChange={e => setName(e.target.value)} />
      <input value={email} onChange={e => setEmail(e.target.value)} />
      <button disabled={isSubmitting}>Submit</button>
    </form>
  );
}
```

**Why it exists:** Different pieces of state change independently. Separate `useState` calls keep each piece simple — you update one without worrying about the others. This is cleaner than one giant state object for simple cases.

**Where it's used:** Forms with multiple fields, components with multiple toggles, any UI with several independent pieces of state.

**What goes wrong without it:**
- One giant state object for everything: `setForm({ ...form, name: "x" })` → must spread every time, easy to forget a field and lose data.
- Calling hooks in different order conditionally → React breaks. Hooks must always be called in the same order, every render.
- Naming collisions: `const [count, setCount]` used twice → second overwrites first. Use descriptive names.

---

## State Batching

**What:** React groups multiple state updates into a single re-render for performance. In React 18, all updates (including async ones) are batched.

```jsx
function Example() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState("");

  const handleClick = () => {
    setCount(1);      // doesn't re-render yet
    setName("Akash"); // doesn't re-render yet
    // React batches both → ONE re-render happens here
  };
}
```

**Why it exists:** Without batching, each `setState` call would trigger a separate re-render. If you update 5 state variables, that's 5 re-renders. Batching does all 5 updates in one re-render — much faster.

**Where it's used:** Any handler that updates multiple state variables at once — form submissions, multi-step updates, toggling loading + data states.

**What goes wrong without it:**
- Expecting intermediate renders: `setCount(1); console.log(count)` → logs old value (0), not 1. State updates are async — the value updates after the re-render.
- Multiple `setCount(count + 1)` calls in one handler → all use the same stale `count`. Use `setCount(prev => prev + 1)` instead.
- Confusion about when re-render happens: it happens AFTER all updates in the handler complete, not after each `setState`.

---

## Object State Updates

**What:** When state is an object, you must spread the old object and override only the changed field. You cannot mutate the object directly.

```jsx
const [form, setForm] = useState({ username: "", email: "", age: 0 });

// Update one field — spread old, override one key
const handleChange = (e) => {
  setForm({ ...form, [e.target.name]: e.target.value });
};
// e.target.name = "email" → updates form.email only

// WRONG:
form.email = "test@test.com";  // mutation — React won't detect
setForm(form);                  // same reference — no re-render
```

**Why it exists:** Objects are passed by reference in JavaScript. If you mutate the same object, React's reference comparison sees no change. Spreading creates a new object with a new reference, so React knows it changed.

**Where it's used:** Forms with multiple fields, user profile updates, settings panels, any state that's a collection of related values.

**What goes wrong without it:**
- `setForm(form)` after mutating → no re-render, UI stays stale.
- Forgetting to spread: `setForm({ email: "x" })` → loses `username` and `age`! They get wiped out. Must spread: `setForm({ ...form, email: "x" })`.
- Deeply nested objects: `setForm({ ...form, address: { city: "NYC" } })` → loses `address.street`. Must spread nested too: `setForm({ ...form, address: { ...form.address, city: "NYC" } })`.

---

## Array State Updates

**What:** When state is an array, you must create a new array (using spread, `.map()`, `.filter()`, `.concat()`) rather than mutating with `.push()`, `.pop()`, `.splice()`.

```jsx
const [todos, setTodos] = useState([
  { id: 1, text: "Learn React", done: false }
]);

// ADD — spread + new item
setTodos([...todos, { id: 2, text: "Build app", done: false }]);

// REMOVE — filter creates new array
setTodos(todos.filter(todo => todo.id !== 1));

// UPDATE — map creates new array
setTodos(todos.map(todo =>
  todo.id === 1 ? { ...todo, done: true } : todo
));

// WRONG — mutates original array
todos.push({ id: 2, text: "Build app" });
setTodos(todos);  // same reference → no re-render
```

**Why it exists:** Same reason as objects — arrays are references. `.push()` mutates the original array (same reference), so React doesn't detect a change. Spread/filter/map always create new arrays (new references).

**Where it's used:** Todo lists, shopping carts, task boards, any list that grows/shrinks/changes.

**What goes wrong without it:**
- `todos.push(newTodo); setTodos(todos)` → same array reference → no re-render → new item doesn't appear.
- `todos[0].done = true; setTodos(todos)` → same reference AND mutated item → React may not detect either change.
- `setTodos(todos.sort())` → `.sort()` mutates the original array! Use `setTodos([...todos].sort())` to sort a copy.

---

## Previous State in Updates

**What:** When updating state based on its previous value, use the functional update form: `setState(prev => newValue)`. This guarantees you're working with the latest state.

```jsx
const [count, setCount] = useState(0);

// RISKY — may use stale state
setCount(count + 1);

// SAFE — always gets latest value
setCount(prev => prev + 1);

// Critical for multiple updates in one handler
const incrementThree = () => {
  setCount(prev => prev + 1);  // 0 → 1
  setCount(prev => prev + 1);  // 1 → 2
  setCount(prev => prev + 1);  // 2 → 3
};
// count is now 3 ✓

// With stale state:
const incrementThreeBad = () => {
  setCount(count + 1);  // 0 + 1 = 1
  setCount(count + 1);  // 0 + 1 = 1 (stale!)
  setCount(count + 1);  // 0 + 1 = 1 (stale!)
};
// count is only 1 ✗
```

**Why it exists:** React batches updates. When you call `setCount(count + 1)` three times, all three use the same `count` from the current render (stale). The functional form queues updates — each receives the result of the previous one.

**Where it's used:** Counters with rapid increments, toggles, adding to arrays based on current array, any state update that depends on the previous value and might be called multiple times.

**What goes wrong without it:**
- `setCount(count + 1)` called 3 times → only +1 instead of +3.
- Async updates: `setTimeout(() => setCount(count + 1), 1000)` → `count` is stale (captured from the render when the timeout was set). Use `setCount(prev => prev + 1)`.
- Toggling: `setToggle(!toggle)` in a loop → same stale issue. Use `setToggle(prev => !prev)`.

---

## Derived State vs Stored State

**What:** Don't store values in state that can be computed from existing state or props. Compute them during render instead.

```jsx
// BAD — storing derived value in state
const [items, setItems] = useState([1, 2, 3]);
const [count, setCount] = useState(3);  // redundant!
// Must manually keep count in sync — error-prone

// GOOD — compute during render
const [items, setItems] = useState([1, 2, 3]);
const count = items.length;  // always correct, no sync needed
```

**Why it exists:** When you store the same data in two places, they can get out of sync. If you add an item but forget to update count, the UI shows wrong data. Computing from the source of truth eliminates this entire class of bugs.

**Where it's used:** List counts, filtered lists, totals, averages, any value that's a function of other state.

**What goes wrong without it:**
- Adding item but forgetting `setCount(count + 1)` → count is wrong.
- Two sources of truth → they disagree → UI shows contradictory data.
- `useEffect` to sync derived state → unnecessary re-renders, potential infinite loops. Just compute in render.
