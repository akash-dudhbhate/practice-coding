# Lesson 04 — Debug Exercises

## Debug 01 (Easy): && with 0
```jsx
{count && <div>{count}</div>}
```
<details><summary>Answer</summary>
**Bug:** When count is 0, `0 && <div>` renders `0` (falsy but rendered). 
**Fix:** `{count > 0 && <div>{count}</div>}` or `{Boolean(count) && ...}`.
</details>

## Debug 02 (Medium): Ternary Returning undefined
```jsx
{isLoggedIn ? <Dashboard /> : null}
```
<details><summary>Answer</summary>
Works but verbose. Can use `&&`: `{isLoggedIn && <Dashboard />}`.
</details>

## Debug 03 (Hard): Condition in Wrong Place
```jsx
function App() {
  if (loading) return <Spinner />;
  return <div>Data: {data}</div>;
  if (error) return <Error />;
}
```
<details><summary>Answer</summary>
**Bug:** `if (error)` is unreachable — after return statement.
**Fix:** Move error check before the data return.
</details>
