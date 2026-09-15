# Lesson 08 — Intuition Checks

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
