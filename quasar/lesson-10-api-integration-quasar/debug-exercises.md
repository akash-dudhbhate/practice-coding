# Lesson 10 — Debug Exercises

## Debug 01 (Easy: No Error Handling
```javascript
async function fetchUsers() {
  const res = await fetch("/api/users");
  return res.json();
}
```
<details><summary>Answer</summary>
**Bug:** No error handling — crashes on network error or non-200 response.
**Fix:** `if (!res.ok) throw new Error("Failed");` and try/catch.
</details>

## Debug 02 (Medium: Not Loading State
```javascript
async function load() {
  const data = await fetchData();
  users.value = data;
}
// no loading indicator
```
<details><summary>Answer</summary>
**Bug:** No loading state — user doesn't know something is happening.
**Fix:** `loading.value = true; try { ... } finally { loading.value = false; }`.
</details>

## Debug 03 (Hard: No Base URL
```javascript
fetch("http://localhost:3000/api/users"); // hardcoded
```
<details><summary>Answer</summary>
**Bug:** Hardcoded URL — breaks in production.
**Fix:** Use env var: `fetch(`${import.meta.env.VITE_API_URL}/users`)`.
</details>
