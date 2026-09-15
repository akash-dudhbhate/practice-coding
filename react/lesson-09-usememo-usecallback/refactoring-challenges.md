# Lesson 09 — Refactoring Challenges

## Refactor 01 (Easy): useMemo for Primitive
### Before
```jsx
const value = useMemo(() => 42, []);
```
### After
```jsx
const value = 42; // primitives don't need memo
```

## Refactor 02 (Medium): Inline Object Prop
### Before
```jsx
<Child style={{ color: 'red' }} onClick={() => doSomething()} />
```
### After
```jsx
const style = useMemo(() => ({ color: 'red' }), []);
const handleClick = useCallback(() => doSomething(), []);
<Child style={style} onClick={handleClick} />
```

## Refactor 03 (Hard): Memo Everything
### Before
```jsx
const a = useMemo(() => x + 1, [x]);
const b = useMemo(() => a * 2, [a]);
const c = useMemo(() => b - 1, [b]);
```
### After
```jsx
const a = x + 1;
const b = a * 2;
const c = b - 1;
// Only memo expensive computations
```
