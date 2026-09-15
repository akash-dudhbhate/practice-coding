# Lesson 10 — Coding Check

## Easy

### p01-solve.vue — Fetch users
- [ ] `fetch()` used to get data
- [ ] Loading state shown
- [ ] Error state shown
- [ ] Data displayed in a list
- [ ] try/catch used
- [ ] `onMounted` used to fetch

### p02-solve.js — Axios instance
- [ ] `axios.create()` used
- [ ] `baseURL` set
- [ ] `timeout` set
- [ ] Request interceptor adds auth token
- [ ] Token read from localStorage
- [ ] Instance exported

### p03-solve.vue — User service + component
- [ ] `userService` with getAll, getById, create, update, delete
- [ ] Component uses the service
- [ ] Loading state shown
- [ ] Error state shown
- [ ] Users displayed

## Medium

### p01-solve.vue — Paginated list
- [ ] Page state (ref)
- [ ] Prev/next buttons
- [ ] Current page displayed
- [ ] Total pages displayed
- [ ] Data fetched per page
- [ ] Navigation works correctly

### p02-solve.vue — Debounced search
- [ ] Quasar's `debounce` used
- [ ] Search input triggers API call
- [ ] Results shown in dropdown
- [ ] Old requests canceled (AbortController or cancel token)
- [ ] No API spam (debounce works)

### p03-solve.vue — Infinite scroll
- [ ] `q-infinite-scroll` used
- [ ] 10 items loaded at a time
- [ ] `@load` handler implemented
- [ ] `done()` called after each load
- [ ] `done(true)` when no more data
- [ ] Loading spinner shown

## Hard

### p01-solve.js — Complete API layer
- [ ] Axios instance with baseURL
- [ ] Request interceptor (auth token)
- [ ] Response interceptor (error handling)
- [ ] Request/response logging
- [ ] Token refresh on 401
- [ ] User service (CRUD)
- [ ] Post service (CRUD)
- [ ] Centralized error handler
- [ ] All exported correctly

### p02-solve.vue — CRUD app
- [ ] List users (with loading state)
- [ ] Create user (form with validation)
- [ ] Edit user (form pre-filled)
- [ ] Delete user (confirm dialog)
- [ ] Notifications on success
- [ ] Notifications on error
- [ ] Loading states per operation
- [ ] List refreshes after CRUD

### p03-solve.vue — useApi composable
- [ ] `useApi` function defined
- [ ] Accepts async function
- [ ] Returns `{ data, loading, error, refetch }`
- [ ] Auto-fetches on mount
- [ ] Used in 3 components (users, posts, comments)
- [ ] Auto-refetch on window focus
- [ ] Manual refetch button
- [ ] Loading/error states work
