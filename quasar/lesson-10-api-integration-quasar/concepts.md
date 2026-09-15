# Lesson 10 — Concepts Explained (API Integration in Quasar)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Fetching Data with fetch()

**What:** Use the browser's `fetch` API to get data from a server.

```js
// Basic fetch
async function fetchUsers() {
    const response = await fetch('https://api.example.com/users')
    const data = await response.json()
    return data
}

// In a component:
import { ref, onMounted } from 'vue'

const users = ref([])
const loading = ref(false)
const error = ref(null)

onMounted(async () => {
    loading.value = true
    try {
        users.value = await fetchUsers()
    } catch (err) {
        error.value = err.message
    } finally {
        loading.value = false
    }
})
```

**Why it exists:** Every app needs data from a server. `fetch` is built-in → no library needed. Understanding it is the foundation of API integration.

**Where it's used:** Every app that communicates with a backend.

**What goes wrong without it:**
- Not handling errors → unhandled rejection → app crashes. Always use try/catch.
- Not checking `response.ok` → 404/500 returns a response, not an error. Check `if (!response.ok) throw new Error()`.
- No loading state → user doesn't know data is loading → thinks app is broken. Always show loading state.

---

## Axios

**What:** A popular HTTP client library — better than fetch for most use cases.

```js
import axios from 'axios'

// GET
const { data } = await axios.get('/api/users')

// POST
const response = await axios.post('/api/users', { name: 'Akash' })

// With params
const { data } = await axios.get('/api/users', {
    params: { page: 1, limit: 10 }
})

// With headers
axios.get('/api/users', {
    headers: { Authorization: `Bearer ${token}` }
})
```

**Why it exists:** `fetch` is low-level — no automatic JSON parsing, no interceptors, no timeouts. Axios provides all of these → cleaner code → less boilerplate.

**Where it's used:** Most Vue/Quasar apps prefer Axios over fetch.

**What goes wrong without it:**
- Not installing: `npm install axios`.
- No base URL → repeating `/api/` everywhere. Create an instance with `baseURL`.
- Not handling errors → axios throws on non-2xx → catch it.

---

## Axios Instance and Interceptors

**What:** Create a configured axios instance with interceptors for auth, logging, error handling.

```js
// src/boot/axios.js
import axios from 'axios'

const api = axios.create({
    baseURL: 'https://api.example.com',
    timeout: 10000,
    headers: { 'Content-Type': 'application/json' }
})

// Request interceptor: add auth token
api.interceptors.request.use(config => {
    const token = localStorage.getItem('token')
    if (token) {
        config.headers.Authorization = `Bearer ${token}`
    }
    return config
})

// Response interceptor: handle errors
api.interceptors.response.use(
    response => response,
    error => {
        if (error.response?.status === 401) {
            // Token expired → redirect to login
            localStorage.removeItem('token')
            window.location.href = '/login'
        }
        return Promise.reject(error)
    }
)

export default api
```

**Why it exists:** Without interceptors, you add auth tokens and handle errors in every API call → duplicated. Interceptors centralize this → DRY → consistent.

**Where it's used:** Every app with auth or centralized error handling.

**What goes wrong without it:**
- Interceptor throwing → request fails silently. Always return the config.
- 401 redirect in interceptor → infinite loop if login page also makes API calls. Check the URL.
- Not rejecting the error in the error interceptor → calling code doesn't know it failed.

---

## API Services Pattern

**What:** Encapsulate API calls in service files → reusable across components.

```js
// src/services/user.js
import api from 'boot/axios'

export const userService = {
    getAll() {
        return api.get('/users')
    },
    getById(id) {
        return api.get(`/users/${id}`)
    },
    create(data) {
        return api.post('/users', data)
    },
    update(id, data) {
        return api.put(`/users/${id}`, data)
    },
    delete(id) {
        return api.delete(`/users/${id}`)
    }
}

// In a component:
import { userService } from 'services/user'
const users = await userService.getAll()
```

**Why it exists:** Without services, API calls are scattered in components → if the endpoint changes, you update every component. Services centralize API calls → one place to change → maintainable.

**Where it's used:** Every app with more than a few API calls.

**What goes wrong without it:**
- Service returning the raw response → components access `response.data` → leaky abstraction. Return `data` directly.
- Not handling errors in the service → components must catch → or the service can catch and return a standard error format.
- Services with state → services should be stateless. Use Pinia for state.

---

## Loading and Error States

**What:** Manage UI states for API calls.

```vue
<template>
    <div>
        <q-spinner v-if="loading" />
        <q-banner v-else-if="error" class="bg-negative">
            {{ error }}
            <q-btn @click="fetchData" label="Retry" />
        </q-banner>
        <div v-else>
            <div v-for="item in data" :key="item.id">{{ item.name }}</div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const data = ref(null)
const loading = ref(false)
const error = ref(null)

async function fetchData() {
    loading.value = true
    error.value = null
    try {
        const response = await fetch('/api/data')
        data.value = await response.json()
    } catch (err) {
        error.value = err.message
    } finally {
        loading.value = false
    }
}
</script>
```

**Why it exists:** Without loading/error states, the user sees nothing during fetch → thinks app is broken. States provide feedback → better UX.

**Where it's used:** Every component that fetches data.

**What goes wrong without it:**
- Only showing data or nothing → user doesn't know if it's loading or failed. Always show all 3 states.
- No retry button on error → user has to refresh the page. Add a retry button.
- Loading state on fast networks → flashes briefly → jarring. Only show after 300ms delay.

---

## Pagination and Infinite Scroll

**What:** Load data in chunks → don't fetch everything at once.

```js
// Pagination
const page = ref(1)
const perPage = ref(10)
const items = ref([])

async function fetchPage() {
    const { data } = await api.get('/items', {
        params: { page: page.value, per_page: perPage.value }
    })
    items.value = data.items
    total.value = data.total
}

// Infinite scroll (Quasar QInfiniteScroll)
<q-infinite-scroll @load="onLoad" :offset="250">
    <div v-for="item in items" :key="item.id">{{ item.name }}</div>
    <template #loading>
        <q-spinner-dots />
    </template>
</q-infinite-scroll>

async function onLoad(index, done) {
    const { data } = await api.get('/items', {
        params: { page: index, per_page: 10 }
    })
    items.value.push(...data.items)
    done(data.items.length === 0)  // true = no more data
}
```

**Why it exists:** Fetching 10,000 items at once → slow, memory-heavy. Pagination/infinite scroll loads in chunks → fast, smooth.

**Where it's used:** Lists, feeds, search results, any large dataset.

**What goes wrong without it:**
- Not calling `done()` in QInfiniteScroll → scroll hangs → no more loading. Always call `done()`.
- Not stopping when no more data → keeps requesting empty pages. Call `done(true)` when empty.
- Appending instead of replacing on page change → duplicate items. Clear `items` before fetching a new page.

---

## Debouncing API Calls

**What:** Delay API calls to avoid spamming the server (e.g., search-as-you-type).

```js
import { debounce } from 'quasar'

const search = debounce(async (query) => {
    if (!query) return
    const { data } = await api.get('/search', { params: { q: query } })
    results.value = data
}, 300)  // wait 300ms after last keystroke

// In template:
<q-input v-model="query" @input="search(query)" label="Search..." />
```

**Why it exists:** Without debounce, every keystroke → API call → 100 calls for "hello" → server overload, rate limits. Debounce waits for the user to stop typing → 1 call → efficient.

**Where it's used:** Search inputs, autocomplete, any input that triggers API calls.

**What goes wrong without it:**
- Debounce too short (50ms) → still too many calls. 300-500ms is typical.
- Debounce too long (2000ms) → feels laggy. User waits 2 seconds for results.
- Not canceling pending requests → old results arrive after new query → wrong results shown. Use AbortController or axios cancel tokens.

---

## Error Handling Patterns

**What:** Consistent error handling across the app.

```js
// Centralized error handler
function handleApiError(error) {
    if (error.response) {
        // Server responded with error status
        const status = error.response.status
        const message = error.response.data.message

        if (status === 401) {
            notify('Session expired. Please login again.', 'negative')
            router.push('/login')
        } else if (status === 403) {
            notify('You do not have permission.', 'negative')
        } else if (status === 404) {
            notify('Resource not found.', 'negative')
        } else if (status >= 500) {
            notify('Server error. Try again later.', 'negative')
        } else {
            notify(message || 'An error occurred.', 'negative')
        }
    } else if (error.request) {
        // No response received (network error)
        notify('Network error. Check your connection.', 'negative')
    } else {
        // Request setup error
        notify('An unexpected error occurred.', 'negative')
    }
}
```

**Why it exists:** Without centralized handling, every component handles errors differently → inconsistent UX. Centralized → consistent → easier to maintain.

**Where it's used:** Every API call — either in the interceptor or in each service.

**What goes wrong without it:**
- Showing raw error messages → might leak server info. Show user-friendly messages.
- Not differentiating error types → 401 (login) and 500 (server) need different handling.
- Silent errors → user doesn't know something failed. Always notify.
