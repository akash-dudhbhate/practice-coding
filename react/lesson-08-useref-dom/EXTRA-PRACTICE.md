# lesson-08-useref-dom — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: useRef vs useState
When should you use useRef?
<details><summary>Answer</summary>
useRef for: DOM access, storing mutable values that DON'T need re-render, keeping values between renders. useState for: values that SHOULD trigger re-render.
</details>

## Check 02: .current
```jsx
const ref = useRef(0);
ref.current = 5; // does this re-render?
```
<details><summary>Answer</summary>
No — ref changes don't trigger re-render. That's the point — refs are for values that persist without causing renders.
</details>

## Check 03: DOM ref
```jsx
const inputRef = useRef();
useEffect(() => {
  inputRef.current.focus();
}, []);
```
<details><summary>Answer</summary>
Access DOM node via `.current`. Common for focus, scroll, measuring elements. Run in useEffect (after DOM is ready).
</details>

## Check 04: Ref persists
```jsx
const ref = useRef(0);
// ref.current is 0 on first render
// ref.current persists across re-renders
```
<details><summary>Answer</summary>
useRef value persists for the lifetime of the component. Doesn't reset on re-render (unlike regular variables).
</details>

## Check 05: forwardRef
```jsx
const MyInput = React.forwardRef((props, ref) => {
  return <input ref={ref} />;
});
```
<details><summary>Answer</summary>
Allows parent to pass ref to a child component's DOM element. Without forwardRef, ref can't be passed to custom components.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Ref on Wrong Element
```jsx
const inputRef = useRef();
return <input ref={inputRef.value} />;
```
<details><summary>Answer</summary>
**Bug:** `ref` should be the ref object itself, not `.value`.
**Fix:** `<input ref={inputRef} />`.
</details>

## Debug 02 (Medium): Ref in Dependencies
```jsx
const inputRef = useRef();
useEffect(() => {
  inputRef.current.focus();
}, [inputRef]);
```
<details><summary>Answer</summary>
**Issue:** `inputRef` itself doesn't change, only `.current` does. React doesn't track `.current` changes.
**Fix:** Remove from deps: `[]` (run once on mount).
</details>

## Debug 03 (Hard): Ref for State
```jsx
const countRef = useRef(0);
const increment = () => { countRef.current++; };
```
<details><summary>Answer</summary>
**Issue:** Changing ref doesn't trigger re-render. UI won't update. Use `useState` for values that should trigger re-render.
**Fix:** `const [count, setCount] = useState(0);`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Using ref for state
```jsx
// WRONG — no re-render
const countRef = useRef(0);
countRef.current++;
// CORRECT — triggers re-render
const [count, setCount] = useState(0);
setCount(count + 1);
```

## Mistake 02: ref={ref.current}
```jsx
// WRONG — passes the value, not the ref object
<input ref={ref.current} />
// CORRECT
<input ref={ref} />
```

## Mistake 03: Ref in dependency array
```jsx
// WRONG — ref object doesn't change
useEffect(() => { ... }, [ref]);
// CORRECT — run once
useEffect(() => { ... }, []);
```

## Mistake 04: Accessing ref before mount
```jsx
const ref = useRef();
ref.current.focus(); // during render — null!
// CORRECT — in useEffect
useEffect(() => { ref.current?.focus(); }, []);
```

## Mistake 05: Not cleaning up refs
```jsx
// Refs to removed elements should be cleared
// to avoid memory leaks
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): useRef for State
### Before
```jsx
const countRef = useRef(0);
countRef.current++;
```
### After
```jsx
const [count, setCount] = useState(0);
setCount(c => c + 1);
```

## Refactor 02 (Medium): QuerySelector
### Before
```jsx
useEffect(() => {
  document.querySelector("#input").focus();
}, []);
```
### After
```jsx
const inputRef = useRef();
useEffect(() => { inputRef.current.focus(); }, []);
<input ref={inputRef} />
```

## Refactor 03 (Hard): Ref for Non-DOM Mutable Value
### Before
```jsx
let timerId; // lost on re-render
useEffect(() => { timerId = setInterval(...); }, []);
```
### After
```jsx
const timerRef = useRef();
useEffect(() => {
  timerRef.current = setInterval(...);
  return () => clearInterval(timerRef.current);
}, []);
```

---

## Approach Comparison — different ways to solve it

## Problem: Focus Input on Mount

### Approach 1: useRef + useEffect
```jsx
const inputRef = useRef();
useEffect(() => { inputRef.current.focus(); }, []);
return <input ref={inputRef} />;
```

### Approach 2: autoFocus attribute
```jsx
<input autoFocus />
```

**Winner:** Approach 2 for simple cases. Approach 1 for conditional focus.

---

## Problem: Store Previous Value

### Approach 1: useRef
```jsx
const prevRef = useRef();
useEffect(() => { prevRef.current = value; });
```

### Approach 2: Custom hook
```jsx
const prevValue = usePrevious(value);
```

**Winner:** Approach 2 — reusable, encapsulated.
