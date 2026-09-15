# Lesson 08 — Common Mistakes

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
