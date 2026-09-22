# lesson-10-api-integration-quasar — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: axios vs fetch
<details><summary>Answer</summary>
axios — interceptors, auto JSON, timeout, better errors. fetch — native, no dependency. Use axios for complex apps, fetch for simple ones.
</details>

## Check 02: Loading states
```javascript
const loading = ref(false);
const error = ref(null);
async function load() {
  loading.value = true; error.value = null;
  try { data.value = await fetchData(); }
  catch (e) { error.value = e.message; }
  finally { loading.value = false; }
}
```
<details><summary>Answer</summary>
Three states: loading, error, data. Template shows spinner, error, or content based on state. Essential for good UX.
</details>

## Check 03: Environment variables
```javascript
// .env
VITE_API_URL=https://api.example.com
// Usage
const url = import.meta.env.VITE_API_URL;
```
<details><summary>Answer</summary>
Vite env vars must start with `VITE_`. Access via `import.meta.env`. Different for dev/production. Never put secrets in frontend env.
</details>

## Check 04: Interceptors
```javascript
axios.interceptors.request.use(config => {
  config.headers.Authorization = `Bearer ${token.value}`;
  return config;
});
```
<details><summary>Answer</summary>
Run before every request/response. Add auth headers, handle errors globally, refresh tokens. Centralized logic.
</details>

## Check 05: Composables for API
```javascript
// useUsers.js
export function useUsers() {
  const users = ref([]);
  const loading = ref(false);
  async function load() { ... }
  return { users, loading, load };
}
```
<details><summary>Answer</summary>
Extract API logic into composables. Reusable across components. Clean separation of concerns.
</details>

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: No error handling
```javascript
// WRONG — crashes silently
const res = await fetch(url);
const data = await res.json();
// CORRECT
try {
  const res = await fetch(url);
  if (!res.ok) throw new Error("Failed");
  const data = await res.json();
} catch (e) { error.value = e.message; }
```

## Mistake 02: No loading state
```javascript
// WRONG — no feedback
async function load() { data.value = await fetch(); }
// CORRECT
async function load() {
  loading.value = true;
  try { data.value = await fetch(); }
  finally { loading.value = false; }
}
```

## Mistake 03: Hardcoded URLs
```javascript
// WRONG
fetch("http://localhost:3000/api")
// CORRECT
fetch(import.meta.env.VITE_API_URL)
```

## Mistake 04: No auth headers
```javascript
// Use interceptor to add auth to all requests
axios.interceptors.request.use(config => {
  config.headers.Authorization = `Bearer ${token}`;
  return config;
});
```

## Mistake 05: Fetching in created instead of onMounted
```javascript
// Use onMounted for initial fetch
onMounted(() => { loadUsers(); });
```

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

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
