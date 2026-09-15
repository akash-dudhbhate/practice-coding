# Lesson 01 — Common Mistakes

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
