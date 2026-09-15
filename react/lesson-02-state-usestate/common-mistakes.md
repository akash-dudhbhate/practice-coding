# Lesson 02 — Common Mistakes

## Mistake 01: Mutating state directly
```jsx
// WRONG
count++;
// CORRECT
setCount(count + 1);
```

## Mistake 02: Mutating object state
```jsx
// WRONG
user.age = 26;
// CORRECT
setUser({ ...user, age: 26 });
```

## Mistake 03: Stale closures
```jsx
// WRONG — uses old count
setCount(count + 1);
setCount(count + 1);
// CORRECT — functional update
setCount(c => c + 1);
setCount(c => c + 1);
```

## Mistake 04: Forgetting to spread arrays
```jsx
// WRONG — mutates original
items.push(newItem);
setItems(items);
// CORRECT
setItems([...items, newItem]);
```

## Mistake 05: Expensive initial state
```jsx
// WRONG — runs every render
const [data] = useState(expensiveFunc());
// CORRECT — runs once
const [data] = useState(() => expensiveFunc());
```
