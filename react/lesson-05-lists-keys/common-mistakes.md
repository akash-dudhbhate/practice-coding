# Lesson 05 — Common Mistakes

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
