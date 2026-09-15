# Lesson 01 — Refactoring Challenges

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
