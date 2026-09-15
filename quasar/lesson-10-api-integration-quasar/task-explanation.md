# Lesson 10 — API Integration in Quasar

## What you'll learn
- Fetching data with fetch()
- Axios (HTTP client library)
- Axios instance and interceptors (auth, error handling)
- API services pattern (encapsulating API calls)
- Loading and error states (UI feedback)
- Pagination and infinite scroll
- Debouncing API calls (search-as-you-type)
- Error handling patterns

## Lesson

### Axios instance
```js
const api = axios.create({ baseURL: 'https://api.example.com' })
api.interceptors.request.use(config => {
    config.headers.Authorization = `Bearer ${token}`
    return config
})
```

### Service pattern
```js
export const userService = {
    getAll: () => api.get('/users'),
    create: (data) => api.post('/users', data),
}
```

### Loading/error states
```vue
<q-spinner v-if="loading" />
<q-banner v-else-if="error" class="bg-negative">{{ error }}</q-banner>
<div v-else>{{ data }}</div>
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.vue` — Create a component that fetches users from a public API (e.g., JSONPlaceholder). Show loading state, error state, and data. Use `fetch()`. Display users in a list.
2. `easy/p02-solve.js` — Create an axios instance with `baseURL`, timeout, and a request interceptor that adds an auth token from localStorage. Export the instance.
3. `easy/p03-solve.vue` — Create a user service (`userService` with getAll, getById, create, update, delete). Create a component that uses it to fetch and display users. Include loading and error states.

### Medium
4. `medium/p01-solve.vue` — Create a paginated list: fetch data page by page. Show page navigation (prev/next). Display current page and total pages. Use the user service.
5. `medium/p02-solve.vue` — Create a search component with debounced API calls. Use Quasar's `debounce` function. Search users by name. Show results in a dropdown. Cancel old requests if a new search starts.
6. `medium/p03-solve.vue` — Create an infinite scroll list using `q-infinite-scroll`. Load 10 items at a time. Stop when no more data. Show a loading spinner during fetch. Use a public API.

### Hard
7. `hard/p01-solve.js` — Build a complete API layer: axios instance with interceptors (auth token, error handling, request/response logging), service files for users and posts, and a centralized error handler. Include token refresh on 401.
8. `hard/p02-solve.vue` — Build a CRUD app: list users, create user (form), edit user (form), delete user (confirm dialog). Use the user service. Show notifications on success/error. Handle loading states for each operation.
9. `hard/p03-solve.vue` — Build a data-fetching composable `useApi`: accepts an async function, returns `{ data, loading, error, refetch }`. Use it in 3 components (users, posts, comments). Include auto-refetch on focus and manual refetch button.

### How to work
- Write your complete JavaScript/Vue solution.
- Remove the TODO comment when done.
- Test by importing into a Quasar app.
