# lesson-01-components-jsx-props — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Component naming
Why must components start with a capital letter?
<details><summary>Answer</summary>
JSX treats lowercase tags as HTML elements (`<div>` → HTML div). Capitalized tags are components (`<MyComponent>` → React component). `<myComponent>` would be treated as HTML.
</details>

## Check 02: Props are read-only
```jsx
function Component({ name }) {
  name = "Other"; // Can you do this?
}
```
<details><summary>Answer</summary>
Technically yes, but it's an anti-pattern. Props are read-only by convention. Never modify props — use state instead.
</details>

## Check 03: JSX is not HTML
```jsx
<div className="box" htmlFor="input">
```
<details><summary>Answer</summary>
JSX uses `className` (not `class`) and `htmlFor` (not `for`) because these are reserved words in JS. Also `onClick` (not `onclick`), camelCase for all attributes.
</details>

## Check 04: Fragment
```jsx
return (<><h1>Title</h1><p>Text</p></>);
```
<details><summary>Answer</summary>
Fragment groups elements without adding extra DOM nodes. `<>` is shorthand for `<React.Fragment>`.
</details>

## Check 05: Expressions in JSX
```jsx
const x = 5;
return <div>{x > 3 ? "big" : "small"}</div>;
```
<details><summary>Answer</summary>
`{}` in JSX evaluates JavaScript expressions. Renders "big". Can't use statements (if, for) — only expressions.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Missing Return
```jsx
function MyComponent() {
  <div>Hello</div>
}
```
<details><summary>Answer</summary>
**Bug:** No `return` statement. Component returns undefined, renders nothing.
**Fix:** `return <div>Hello</div>;`
</details>

## Debug 02 (Medium): Props Not Destructured
```jsx
function Greeting(props) {
  return <h1>Hello, {Props.name}</h1>
}
```
<details><summary>Answer</summary>
**Bug:** `Props` (capital P) — JavaScript is case-sensitive. `props` is the parameter.
**Fix:** `return <h1>Hello, {props.name}</h1>` or destructure: `function Greeting({ name }) {`.
</details>

## Debug 03 (Hard): JSX Expression Not Wrapped
```jsx
function App() {
  return (
    <h1>Title</h1>
    <p>Content</p>
  );
}
```
<details><summary>Answer</summary>
**Bug:** Adjacent JSX elements must be wrapped. Can't return multiple elements.
**Fix:** Wrap in fragment: `<>...</>` or `<div>...</div>`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Lowercase component names
```jsx
// WRONG — treated as HTML
function myComponent() { ... }
// CORRECT — capital letter
function MyComponent() { ... }
```

## Mistake 02: class instead of className
```jsx
// WRONG
<div class="box">
// CORRECT
<div className="box">
```

## Mistake 03: Multiple elements without wrapper
```jsx
// WRONG
return <h1>A</h1><p>B</p>;
// CORRECT
return <><h1>A</h1><p>B</p></>;
```

## Mistake 04: Forgetting return
```jsx
// WRONG — renders nothing
function Comp() { <div />; }
// CORRECT
function Comp() { return <div />; }
```

## Mistake 05: Using statements in JSX
```jsx
// WRONG — can't use if in JSX
<div>{if (x) "yes"}</div>
// CORRECT — use ternary
<div>{x ? "yes" : null}</div>
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Props Destructuring
### Before
```jsx
function User(props) {
  return <div>{props.name} - {props.age}</div>;
}
```
### After
```jsx
function User({ name, age }) {
  return <div>{name} - {age}</div>;
}
```

## Refactor 02 (Medium): Inline Styles
### Before
```jsx
<div style={{ color: 'red', fontSize: '18px', margin: '10px' }}>Error</div>
```
### After
```jsx
<div className="error">Error</div>
```

## Refactor 03 (Hard): God Component
### Before
```jsx
function Page() {
  const [user, setUser] = useState(null);
  const [posts, setPosts] = useState([]);
  // fetch user, fetch posts, render header, sidebar, feed, footer
}
```
### After
```jsx
function Page() {
  return <><Header /><Sidebar /><Feed /><Footer /></>;
}
```

---

## Approach Comparison — different ways to solve it

## Problem: Greeting Component

### Approach 1: props object
```jsx
function Greeting(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

### Approach 2: Destructured props
```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}</h1>;
}
```

**Winner:** Approach 2 — cleaner, explicit about what props are used.

---

## Problem: Multiple Elements

### Approach 1: Wrapper div
```jsx
return <div><h1>A</h1><p>B</p></div>;
```
**Cons:** Extra DOM node, may break flexbox/grid.

### Approach 2: Fragment
```jsx
return <><h1>A</h1><p>B</p></>;
```

**Winner:** Approach 2 — no extra DOM node.
