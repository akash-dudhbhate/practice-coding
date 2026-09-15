# Lesson 16 — Concepts Explained (React Query / TanStack Query)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is React Query?

**What:** React Query is a data-fetching and state management library for async data. It handles caching, background updates, stale data, retries, and more.

```jsx
import { useQuery } from '@tanstack/react-query';

function UserProfile({ userId }) {
    const { data, isLoading, error } = useQuery({
        queryKey: ['user', userId],
        queryFn: () => fetch(`/api/users/${userId}`).then(res => res.json()),
    });

    if (isLoading) return <p>Loading...</p>;
    if (error) return <p>Error: {error.message}</p>;
    return <h1>{data.name}</h1>;
}
```

**Why it exists:** Without React Query, you write custom hooks with `useEffect` + `useState` for loading/error/data, manual caching, retry logic, background refetching, and stale data handling → 100+ lines per data source. React Query handles all of this declaratively.

**Where it's used:** Every app that fetches data from an API — dashboards, lists, profiles, real-time data.

**What goes wrong without it:**
- Forgetting to install: `@tanstack/react-query` (v4+) or `react-query` (v3). The package was renamed. Use the new one.
- No `QueryClientProvider` → `useQuery` throws error. Must wrap the app in a provider.
- Query keys must be unique and serializable. Objects with functions → key comparison fails.

---

## QueryClient and Provider

**What:** The `QueryClient` is the central cache. The provider makes it available to all components.

```jsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient({
    defaultOptions: {
        queries: {
            staleTime: 60 * 1000,       // data is fresh for 1 minute
            cacheTime: 5 * 60 * 1000,   // cache kept for 5 minutes after unmount
            retry: 3,                    // retry failed requests 3 times
            refetchOnWindowFocus: true,  // refetch when user returns to tab
        },
    },
});

function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <MyApp />
        </QueryClientProvider>
    );
}
```

**Why it exists:** Without a central cache, each component manages its own data → duplicate requests, no sharing, no consistency. The `QueryClient` is the single source of truth → all components share cached data.

**Where it's used:** At the app root — wrap everything in `QueryClientProvider`.

**What goes wrong without it:**
- Creating `QueryClient` inside the component → new client every render → cache is lost. Create it OUTSIDE the component (module level or `useRef`).
- `staleTime: 0` (default) → data is immediately stale → refetches on every mount/focus. Set a reasonable `staleTime`.
- `refetchOnWindowFocus: true` → every tab switch triggers refetch → too many requests for some APIs. Disable if needed.

---

## useQuery

**What:** The primary hook for fetching data.

```jsx
function ProductList() {
    const { data, isLoading, error, refetch, isFetching } = useQuery({
        queryKey: ['products'],
        queryFn: () => fetch('/api/products').then(res => res.json()),
        staleTime: 30000,  // 30 seconds
    });

    // States:
    // isLoading: first load, no data yet
    // isFetching: any fetch in progress (including background refetch)
    // data: the fetched data (undefined while loading)
    // error: error object if fetch failed

    if (isLoading) return <Skeleton />;
    if (error) return <ErrorMessage error={error} />;

    return (
        <>
            {isFetching && <RefetchIndicator />}
            {data.map(product => <ProductCard key={product.id} product={product} />)}
            <button onClick={refetch}>Refresh</button>
        </>
    );
}
```

**Why it exists:** Without `useQuery`, you write:
```jsx
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);
useEffect(() => {
    let cancelled = false;
    setLoading(true);
    fetch('/api/products')
        .then(res => res.json())
        .then(data => { if (!cancelled) setData(data); })
        .catch(err => { if (!cancelled) setError(err); })
        .finally(() => { if (!cancelled) setLoading(false); });
    return () => { cancelled = true; };
}, []);
```
→ 15 lines of boilerplate. `useQuery` does it in 4 lines + handles caching, refetching, retries.

**Where it's used:** Every data-fetching component.

**What goes wrong without it:**
- `isLoading` vs `isFetching`: `isLoading` = first load (no data). `isFetching` = any fetch (including background). Using `isLoading` for background refetch indicator → never shows. Use `isFetching`.
- `queryFn` must return a Promise. Forgetting `return` → queryFn returns `undefined` → error.
- Throwing in `queryFn` → React Query catches it → sets `error`. Don't try/catch inside queryFn (let RQ handle it).

---

## Query Keys

**What:** Query keys uniquely identify a query in the cache. They're arrays that can contain strings, numbers, and objects.

```jsx
// Simple key
useQuery({ queryKey: ['products'], queryFn: ... });

// Key with parameter
useQuery({ queryKey: ['user', userId], queryFn: ... });

// Key with multiple parameters
useQuery({ queryKey: ['posts', userId, { sort: 'desc' }], queryFn: ... });

// Same key → same cache entry
// ['user', 1] and ['user', 2] → different cache entries
// ['user', 1] and ['user', 1] → same cache entry (shared data)
```

**Why it exists:** Without query keys, React Query can't know which queries to share, refetch, or invalidate. Keys are the cache addresses → same key = same data.

**Where it's used:** Every `useQuery` call. Also used for invalidation (`queryClient.invalidateQueries(['products'])`).

**What goes wrong without it:**
- Key with an object → React Query serializes it for comparison. `{ sort: 'desc' }` and `{ sort: 'desc' }` → same key (deep equality). But `{a: 1, b: 2}` and `{b: 2, a: 1}` → same key (order doesn't matter).
- Key with a function → can't serialize → comparison fails. Use primitive values (strings, numbers).
- Inconsistent keys: `['users']` in one place, `['user']` in another → two separate cache entries → duplicate requests. Be consistent.

---

## useMutation

**What:** `useMutation` handles data modifications (create, update, delete).

```jsx
import { useMutation, useQueryClient } from '@tanstack/react-query';

function AddProduct() {
    const queryClient = useQueryClient();

    const mutation = useMutation({
        mutationFn: (newProduct) => fetch('/api/products', {
            method: 'POST',
            body: JSON.stringify(newProduct),
        }).then(res => res.json()),
        onSuccess: () => {
            // Invalidate and refetch the products list
            queryClient.invalidateQueries({ queryKey: ['products'] });
        },
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        mutation.mutate({ name: "New Product", price: 99.99 });
    };

    return (
        <form onSubmit={handleSubmit}>
            <button disabled={mutation.isPending}>
                {mutation.isPending ? 'Adding...' : 'Add Product'}
            </button>
            {mutation.isError && <p>Error: {mutation.error.message}</p>}
            {mutation.isSuccess && <p>Added successfully!</p>}
        </form>
    );
}
```

**Why it exists:** Without `useMutation`, you write custom async handlers with loading/error/success states → boilerplate. `useMutation` handles states, retries, and cache invalidation → clean.

**Where it's used:** Forms, delete buttons, any data modification.

**What goes wrong without it:**
- Forgetting `invalidateQueries` → the list doesn't update after adding → stale data. Always invalidate related queries on success.
- `mutation.isPending` (v5) vs `mutation.isLoading` (v3/v4) → API changed. Check your version.
- `mutate` is not a promise → can't `await mutate(data)`. Use `mutateAsync` if you need to await.

---

## Cache Invalidation

**What:** Tell React Query that cached data is stale and should be refetched.

```jsx
const queryClient = useQueryClient();

// Invalidate all queries with keys starting with 'products'
queryClient.invalidateQueries({ queryKey: ['products'] });

// Invalidate a specific query
queryClient.invalidateQueries({ queryKey: ['user', 5] });

// Invalidate all queries
queryClient.invalidateQueries();

// Remove a query from cache entirely (no refetch)
queryClient.removeQueries({ queryKey: ['old-data'] });

// Set data manually (optimistic update)
queryClient.setQueryData(['products'], (oldData) => [...oldData, newProduct]);
```

**Why it exists:** After a mutation (add/update/delete), the cached list data is stale → needs refetching. Invalidation marks the query as stale → next render or `refetchOnWindowFocus` triggers a refetch.

**Where it's used:** After every mutation — `onSuccess` callback of `useMutation`.

**What goes wrong without it:**
- Invalidating too broadly → all queries refetch → too many requests. Be specific with keys.
- Forgetting to invalidate → UI shows stale data → user thinks their action didn't work.
- `invalidateQueries` → marks as stale + refetches active queries. Inactive queries refetch on next use. If you want immediate refetch, the query must be "active" (component is mounted).

---

## Optimistic Updates

**What:** Update the UI immediately (before the server responds), then roll back if the request fails.

```jsx
const mutation = useMutation({
    mutationFn: (newTodo) => fetch('/api/todos', { method: 'POST', body: JSON.stringify(newTodo) }),

    // Before the mutation runs → update cache optimistically
    onMutate: async (newTodo) => {
        await queryClient.cancelQueries({ queryKey: ['todos'] });
        const previousTodos = queryClient.getQueryData(['todos']);
        queryClient.setQueryData(['todos'], (old) => [...old, newTodo]);
        return { previousTodos };  // context for rollback
    },

    // If mutation fails → roll back
    onError: (err, newTodo, context) => {
        queryClient.setQueryData(['todos'], context.previousTodos);
    },

    // Always refetch after success or error
    onSettled: () => {
        queryClient.invalidateQueries({ queryKey: ['todos'] });
    },
});
```

**Why it exists:** Without optimistic updates, the user waits for the server response before seeing the change → feels slow. Optimistic updates show the change instantly → fast UX. If the server rejects → roll back → user sees the reversion.

**Where it's used:** Todo apps (instant add), likes/upvotes, toggles, any action that should feel instant.

**What goes wrong without it:**
- Forgetting `onError` rollback → if the mutation fails, the optimistic update stays → UI shows data that doesn't exist on the server.
- Not cancelling in-flight queries → `onMutate` runs while a fetch is in progress → fetch overwrites the optimistic update → flicker.
- Optimistic updates for critical data (payments, orders) → if it fails, user thinks it succeeded → worse than waiting. Use optimistic updates only for non-critical data.

---

## Pagination and Infinite Queries

**What:** React Query has built-in support for pagination and infinite scrolling.

```jsx
// Pagination
function PaginatedList() {
    const [page, setPage] = useState(1);
    const { data, isLoading } = useQuery({
        queryKey: ['products', page],
        queryFn: () => fetch(`/api/products?page=${page}`).then(res => res.json()),
        keepPreviousData: true,  // v4; in v5 use placeholderData: keepPreviousData
    });

    return (
        <>
            {data?.items.map(item => <div key={item.id}>{item.name}</div>)}
            <button onClick={() => setPage(p => Math.max(1, p - 1))}>Prev</button>
            <span>Page {page}</span>
            <button onClick={() => setPage(p => p + 1)}>Next</button>
        </>
    );
}

// Infinite scroll
import { useInfiniteQuery } from '@tanstack/react-query';

function InfiniteList() {
    const {
        data,
        fetchNextPage,
        hasNextPage,
        isFetchingNextPage,
    } = useInfiniteQuery({
        queryKey: ['products'],
        queryFn: ({ pageParam = 1 }) => fetch(`/api/products?page=${pageParam}`).then(res => res.json()),
        getNextPageParam: (lastPage) => lastPage.nextPage ?? undefined,
    });

    return (
        <>
            {data.pages.map((page, i) => (
                <div key={i}>
                    {page.items.map(item => <div key={item.id}>{item.name}</div>)}
                </div>
            ))}
            <button
                onClick={() => fetchNextPage()}
                disabled={!hasNextPage || isFetchingNextPage}
            >
                {isFetchingNextPage ? 'Loading...' : 'Load More'}
            </button>
        </>
    );
}
```

**Why it exists:** Without React Query's pagination support, you manage page state, loading states, and cache manually → complex. `useInfiniteQuery` handles all of it → clean infinite scroll.

**Where it's used:** Product lists, feeds, search results, comment threads.

**What goes wrong without it:**
- `keepPreviousData` → without it, switching pages shows a loading flash. With it, previous page stays visible while next loads → smoother.
- `getNextPageParam` must return `undefined` when there are no more pages → `hasNextPage` becomes false → "Load More" button disables.
- `data.pages` is an array of pages → must map through both levels. Forgetting the outer map → only shows the last page.
