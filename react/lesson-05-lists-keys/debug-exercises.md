# Lesson 05 — Debug Exercises

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
