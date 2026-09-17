# lesson-05-lists-keys — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Why keys?
Why does React need keys for list items?
<details><summary>Answer</summary>
Keys help React identify which items changed, were added, or removed. Without keys, React re-renders all items. With keys, React updates only changed items.
</details>

## Check 02: Key uniqueness
Must keys be globally unique?
<details><summary>Answer</summary>
No — keys must be unique among SIBLINGS. Two lists can have items with the same key.
</details>

## Check 03: When is index as key OK?
<details><summary>Answer</summary>
Only when: list is static (never reorders), items have no state, list never filters/sorts. Otherwise, use stable IDs.
</details>

## Check 04: map returns
```jsx
{items.map(item => <div key={item.id}>{item.name}</div>)}
```
<details><summary>Answer</summary>
`map` returns an array of elements. React renders arrays. Each element needs a key.
</details>

## Check 05: Fragment in map
```jsx
{items.map(item => (
  <React.Fragment key={item.id}>
    <dt>{item.term}</dt>
    <dd>{item.desc}</dd>
  </React.Fragment>
))}
```
<details><summary>Answer</summary>
Fragment can have a key when in a map. `<>` shorthand can't take key — use `<React.Fragment key={...}>`.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Missing Key
```jsx
{items.map(item => <li>{item.name}</li>)}
```
<details><summary>Answer</summary>
**Bug:** No `key` prop — React warns and may have rendering bugs.
**Fix:** `<li key={item.id}>{item.name}</li>`.
</details>

## Debug 02 (Medium): Index as Key
```jsx
{items.map((item, index) => <li key={index}>{item.name}</li>)}
```
<details><summary>Answer</summary>
**Issue:** Index as key causes bugs when list reorders, inserts, or deletes. React may render wrong items.
**Fix:** Use stable unique ID: `key={item.id}`.
</details>

## Debug 03 (Hard): Key on Wrong Element
```jsx
{items.map(item => (
  <div>
    <li key={item.id}>{item.name}</li>
  </div>
))}
```
<details><summary>Answer</summary>
**Bug:** Key is on `<li>` but the outer `<div>` is the repeated element. Key should be on the outermost element in the map.
**Fix:** `<div key={item.id}><li>...</li></div>`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Missing keys
```jsx
// WRONG — React warning
{items.map(item => <li>{item.name}</li>)}
// CORRECT
{items.map(item => <li key={item.id}>{item.name}</li>)}
```

## Mistake 02: Index as key
```jsx
// WRONG — bugs on reorder
{items.map((item, i) => <li key={i}>...)}
// CORRECT — stable ID
{items.map(item => <li key={item.id}>...)}
```

## Mistake 03: Key on wrong element
```jsx
// WRONG — key on inner element
items.map(item => <div><li key={item.id}>...</li></div>)
// CORRECT — key on outer
items.map(item => <div key={item.id}><li>...</li></div>)
```

## Mistake 04: Non-unique keys
```jsx
// WRONG — duplicate keys
{items.map(item => <li key="item">...</li>)}
```

## Mistake 05: Using <> with key
```jsx
// WRONG — shorthand fragment can't take key
{items.map(item => <>...</>)}
// CORRECT
{items.map(item => <Fragment key={item.id}>...</Fragment>)}
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Index as Key
### Before
```jsx
{items.map((item, index) => <li key={index}>{item.name}</li>)}
```
### After
```jsx
{items.map(item => <li key={item.id}>{item.name}</li>)}
```

## Refactor 02 (Medium): No Key
### Before
```jsx
{items.map(item => <li>{item.name}</li>)}
```
### After
```jsx
{items.map(item => <li key={item.id}>{item.name}</li>)}
```

## Refactor 03 (Hard): Inline Map
### Before
```jsx
function List({ items }) {
  return <ul>{items.map(item => <li key={item.id}>{item.name} - {item.price}</li>)}</ul>;
}
```
### After
```jsx
const ListItem = ({ item }) => <li>{item.name} - {item.price}</li>;
function List({ items }) {
  return <ul>{items.map(item => <ListItem key={item.id} item={item} />)}</ul>;
}
```

---

## Approach Comparison — different ways to solve it

## Problem: Render List

### Approach 1: for loop
```jsx
const elements = [];
for (let item of items) {
  elements.push(<li key={item.id}>{item.name}</li>);
}
return <ul>{elements}</ul>;
```

### Approach 2: map
```jsx
return <ul>{items.map(item => <li key={item.id}>{item.name}</li>)}</ul>;
```

**Winner:** Approach 2 — declarative, idiomatic React.

---

## Problem: Key Strategy

### Approach 1: Index
```jsx
key={index}
```
**Cons:** Breaks on reorder/insert/delete.

### Approach 2: ID
```jsx
key={item.id}
```

**Winner:** Approach 2 — always use stable unique IDs.
