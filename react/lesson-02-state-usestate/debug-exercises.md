# Lesson 02 — Debug Exercises

## Debug 01 (Easy): Direct State Mutation
```jsx
const [count, setCount] = useState(0);
count = count + 1;
```
<details><summary>Answer</summary>
**Bug:** Directly modifying state variable. React doesn't detect the change, no re-render.
**Fix:** `setCount(count + 1);`
</details>

## Debug 02 (Medium): Stale Closure
```jsx
const [count, setCount] = useState(0);
const increment = () => {
  setCount(count + 1);
  setCount(count + 1);
};
```
<details><summary>Answer</summary>
**Bug:** Both calls use the same `count` value (stale closure). Only increments by 1.
**Fix:** Use functional update: `setCount(c => c + 1); setCount(c => c + 1);`
</details>

## Debug 03 (Hard): Object State Mutation
```jsx
const [user, setUser] = useState({ name: "A", age: 25 });
user.age = 26;
```
<details><summary>Answer</summary>
**Bug:** Mutating state object directly. React doesn't detect the change.
**Fix:** `setUser({ ...user, age: 26 });` — create new object.
</details>
