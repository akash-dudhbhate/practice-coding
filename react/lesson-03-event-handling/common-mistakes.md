# Lesson 03 — Common Mistakes

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
