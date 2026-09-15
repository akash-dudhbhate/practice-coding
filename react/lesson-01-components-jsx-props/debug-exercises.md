# Lesson 01 — Debug Exercises

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
