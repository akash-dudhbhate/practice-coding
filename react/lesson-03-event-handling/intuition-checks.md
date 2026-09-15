# Lesson 03 — Intuition Checks

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
