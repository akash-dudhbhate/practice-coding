# Lesson 20 — Refactoring Challenges

## Refactor 01 (Easy): No Memo on Expensive List
### Before
```jsx
function List({ items }) {
  const sorted = items.sort((a, b) => a.name.localeCompare(b.name));
  return sorted.map(i => <Item key={i.id} item={i} />);
}
```
### After
```jsx
const sorted = useMemo(() => [...items].sort((a, b) => a.name.localeCompare(b.name)), [items]);
```

## Refactor 02 (Medium): No React.memo
### Before
```jsx
function Item({ item }) { return <div>{item.name}</div>; }
// re-renders even if item prop same
```
### After
```jsx
const Item = React.memo(({ item }) => <div>{item.name}</div>);
```

## Refactor 03 (Hard: Inline Object Props
### Before
```jsx
<Child style={{ color: 'red' }} config={{ timeout: 1000 }} />
```
### After
```jsx
const style = useMemo(() => ({ color: 'red' }), []);
const config = useMemo(() => ({ timeout: 1000 }), []);
<Child style={style} config={config} />
```
