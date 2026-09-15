# Lesson 10 — Intuition Checks

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
