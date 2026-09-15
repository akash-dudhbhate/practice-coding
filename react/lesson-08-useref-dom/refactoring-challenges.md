# Lesson 08 — Refactoring Challenges

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
