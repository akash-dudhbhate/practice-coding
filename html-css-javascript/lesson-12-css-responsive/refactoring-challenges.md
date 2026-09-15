# Lesson 12 — Refactoring Challenges

## Refactor 01 (Easy): No JSON Parse on Get
### Before
```javascript
const user = localStorage.getItem("user");
const name = JSON.parse(user).name;
```
### After
```javascript
const user = JSON.parse(localStorage.getItem("user") || "{}");
const name = user.name;
```

## Refactor 02 (Medium): Repeated localStorage Code
### Before
```javascript
localStorage.setItem("theme", JSON.stringify(theme));
const t = JSON.parse(localStorage.getItem("theme"));
```
### After
```javascript
const store = {
  get: (k) => JSON.parse(localStorage.getItem(k) || "null"),
  set: (k, v) => localStorage.setItem(k, JSON.stringify(v)),
};
store.set("theme", theme);
const t = store.get("theme");
```

## Refactor 03 (Hard): No Error Handling on Parse
### Before
```javascript
const data = JSON.parse(localStorage.getItem("data"));
```
### After
```javascript
function safeParse(key, fallback = null) {
  try { return JSON.parse(localStorage.getItem(key)); }
  catch { return fallback; }
}
const data = safeParse("data", {});
```
