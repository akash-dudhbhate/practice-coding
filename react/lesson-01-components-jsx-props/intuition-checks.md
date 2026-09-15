# Lesson 01 — Intuition Checks

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
