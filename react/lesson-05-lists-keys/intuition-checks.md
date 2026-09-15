# Lesson 05 — Intuition Checks

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
