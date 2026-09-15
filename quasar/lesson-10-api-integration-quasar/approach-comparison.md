# Lesson 10 — Approach Comparison

## Problem: API Calls

### Approach 1: fetch
```javascript
const res = await fetch(url, { headers: { Authorization: `Bearer ${token}` } });
const data = await res.json();
```

### Approach 2: axios
```javascript
const { data } = await axios.get(url);
```

**Winner:** Approach 2 — interceptors, auto JSON, better errors.

---

## Problem: Data Fetching Pattern

### Approach 1: In component
```javascript
onMounted(async () => { users.value = await fetchUsers(); });
```

### Approach 2: Composable
```javascript
const { users, loading, load } = useUsers();
onMounted(load);
```

**Winner:** Approach 2 — reusable, testable, clean.
