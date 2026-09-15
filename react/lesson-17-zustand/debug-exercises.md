# Lesson 17 — Debug Exercises

## Debug 01 (Easy: Selecting Entire Store
```jsx
const store = useStore();
// re-renders on ANY state change
```
<details><summary>Answer</summary>
**Bug:** Selecting entire store causes re-render on any change, even unrelated ones.
**Fix:** `const count = useStore(s => s.count);` — select only what you need.
</details>

## Debug 02 (Medium): Mutating State Directly
```jsx
const increment = () => { count++; };
```
<details><summary>Answer</summary>
**Bug:** Direct mutation — Zustand won't detect change.
**Fix:** `set({ count: count + 1 });` or `set(state => ({ count: state.count + 1 }));`.
</details>

## Debug 03 (Hard): Creating Store Inside Component
```jsx
function App() {
  const store = createStore(...);
}
```
<details><summary>Answer</summary>
**Bug:** New store on every render. State doesn't persist.
**Fix:** Create store at module level: `const useStore = create(...)`.
</details>
