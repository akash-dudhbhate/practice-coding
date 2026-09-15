# Lesson 06 — Refactoring Challenges

## Refactor 01 (Easy): No Dependency Array
### Before
```jsx
useEffect(() => { fetchData(); }); // runs every render
```
### After
```jsx
useEffect(() => { fetchData(); }, []); // runs once
```

## Refactor 02 (Medium): Missing Dependency
### Before
```jsx
useEffect(() => { setUser(currentUser); }, []); // stale currentUser
```
### After
```jsx
useEffect(() => { setUser(currentUser); }, [currentUser]);
```

## Refactor 03 (Hard): Effect for Derived Data
### Before
```jsx
const [total, setTotal] = useState(0);
useEffect(() => { setTotal(items.reduce((s, i) => s + i.price, 0)); }, [items]);
```
### After
```jsx
const total = useMemo(() => items.reduce((s, i) => s + i.price, 0), [items]);
```
