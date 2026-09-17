# lesson-03-event-handling — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: onClick syntax
```jsx
<button onClick={handleClick}>     // A
<button onClick={() => handleClick()}>  // B
```
<details><summary>Answer</summary>
A passes the function reference. B creates a new arrow function that calls handleClick. Both work. A is slightly more efficient (no new function each render).
</details>

## Check 02: Event object
```jsx
const handleClick = (e) => {
  console.log(e.type);    // "click"
  console.log(e.target);  // the element
};
```
<details><summary>Answer</summary>
React wraps native events in SyntheticEvent for cross-browser compatibility. Has same API as native events.
</details>

## Check 03: preventDefault
```jsx
const handleSubmit = (e) => {
  e.preventDefault();
  // save data
};
```
<details><summary>Answer</summary>
Stops default form submission (page reload). Same as vanilla JS.
</details>

## Check 04: Passing arguments
```jsx
<button onClick={() => deleteItem(id)}>Delete</button>
```
<details><summary>Answer</summary>
Arrow function wraps the call so it's not executed during render. The arrow function is the event handler, which calls deleteItem with the id.
</details>

## Check 05: this in class components
```jsx
class Component extends React.Component {
  handleClick() { console.log(this); }
  render() {
    return <button onClick={this.handleClick}>Click</button>;
  }
}
```
<details><summary>Answer</summary>
`this` is undefined — method isn't bound. Fix: `onClick={this.handleClick.bind(this)}` or use arrow function: `handleClick = () => {...}`.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Calling Function Immediately
```jsx
<button onClick={handleClick()}>Click</button>
```
<details><summary>Answer</summary>
**Bug:** `handleClick()` is called during render, not on click.
**Fix:** `onClick={handleClick}` (pass reference, don't call).
</details>

## Debug 02 (Medium): Missing Parameter
```jsx
{items.map(item => (
  <button onClick={deleteItem(item.id)}>Delete</button>
))}
```
<details><summary>Answer</summary>
**Bug:** `deleteItem(item.id)` is called immediately during render.
**Fix:** `onClick={() => deleteItem(item.id)}`.
</details>

## Debug 03 (Hard): Synthetic Event Pooling
```jsx
const handleClick = (e) => {
  setTimeout(() => {
    console.log(e.target.value); // may be null
  }, 100);
};
```
<details><summary>Answer</summary>
**Bug:** React reuses synthetic events. `e` is nullified after the handler. (Note: React 17+ doesn't pool events, but older code may have this issue.)
**Fix:** Extract value before async: `const value = e.target.value;`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Calling function in JSX
```jsx
// WRONG — runs immediately
<button onClick={handleClick()}>
// CORRECT — pass reference
<button onClick={handleClick}>
```

## Mistake 02: Not using arrow for parameters
```jsx
// WRONG — runs immediately
<button onClick={deleteItem(id)}>
// CORRECT — wrap in arrow
<button onClick={() => deleteItem(id)}>
```

## Mistake 03: Forgetting preventDefault
```jsx
// WRONG — page reloads
<form onSubmit={handleSubmit}>
// CORRECT
const handleSubmit = (e) => { e.preventDefault(); ... };
```

## Mistake 04: Inline function in render
```jsx
// Creates new function every render — ok for simple cases
// But can cause performance issues with memoized children
<button onClick={() => doSomething()}>
```

## Mistake 05: Not binding in class components
```jsx
// WRONG — this is undefined
class C extends React.Component {
  handleClick() { this.setState(...); }
  render() { return <button onClick={this.handleClick} />; }
}
// CORRECT — arrow function class field
class C extends React.Component {
  handleClick = () => { this.setState(...); };
}
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Inline Handler
### Before
```jsx
<button onClick={() => setCount(count + 1)}>+</button>
```
### After
```jsx
const increment = () => setCount(c => c + 1);
<button onClick={increment}>+</button>
```

## Refactor 02 (Medium): No PreventDefault
### Before
```jsx
function handleSubmit() { fetch("/api", { method: "POST" }); }
<form onSubmit={handleSubmit}>
```
### After
```jsx
function handleSubmit(e) { e.preventDefault(); fetch("/api", { method: "POST" }); }
```

## Refactor 03 (Hard): Inline Function in Props
### Before
```jsx
<List renderItem={(item) => <div key={item.id}>{item.name}</div>} />
```
### After
```jsx
const renderItem = useCallback((item) => <div key={item.id}>{item.name}</div>, []);
<List renderItem={renderItem} />
```

---

## Approach Comparison — different ways to solve it

## Problem: Click Handler with Parameter

### Approach 1: Arrow function
```jsx
<button onClick={() => deleteItem(id)}>Delete</button>
```

### Approach 2: bind
```jsx
<button onClick={deleteItem.bind(null, id)}>Delete</button>
```

**Winner:** Approach 1 — more readable, more common.

---

## Problem: Form Submission

### Approach 1: Button onClick
```jsx
<button onClick={handleSubmit}>Submit</button>
```
**Cons:** Doesn't handle Enter key.

### Approach 2: Form onSubmit
```jsx
<form onSubmit={handleSubmit}>
  <button type="submit">Submit</button>
</form>
```

**Winner:** Approach 2 — handles all submission methods.
