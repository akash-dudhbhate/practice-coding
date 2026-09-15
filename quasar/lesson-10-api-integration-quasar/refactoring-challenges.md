# Lesson 10 — Refactoring Challenges

## Refactor 01 (Easy): No Error Handling
### Before
```javascript
const data = await fetch(url).then(r => r.json());
```
### After
```javascript
try {
  const res = await fetch(url);
  if (!res.ok) throw new Error("Failed");
  const data = await res.json();
} catch (e) { error.value = e.message; }
```

## Refactor 02 (Medium): Hardcoded URL
### Before
```javascript
fetch("http://localhost:3000/api")
```
### After
```javascript
fetch(import.meta.env.VITE_API_URL)
```

## Refactor 03 (Hard: API Logic in Component
### Before
```javascript
onMounted(async () => { users.value = await fetchUsers(); });
```
### After
```javascript
const { users, loading, load } = useUsers();
onMounted(load);
```
