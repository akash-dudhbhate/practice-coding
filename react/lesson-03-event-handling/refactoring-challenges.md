# Lesson 03 — Refactoring Challenges

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
