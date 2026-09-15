# Lesson 10 — Common Mistakes

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
