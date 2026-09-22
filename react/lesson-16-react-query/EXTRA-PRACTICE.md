# lesson-16-react-query — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Query key
What is a query key?
<details><summary>Answer</summary>
Array that uniquely identifies a query. Used for caching, refetching, and invalidation. `["users", userId]` — different userId = different cache entry.
</details>

## Check 02: useQuery return
```jsx
const { data, isLoading, error, refetch } = useQuery(...);
```
<details><summary>Answer</summary>
`data` — response, `isLoading` — first load, `error` — fetch error, `refetch` — manual refetch. Also `isFetching`, `isStale`, `status`.
</details>

## Check 03: Stale time
```jsx
useQuery("key", fn, { staleTime: 5000 });
```
<details><summary>Answer</summary>
Data is considered fresh for 5 seconds. Refetches on window focus or mount only after stale. Default: 0 (always stale).
</details>

## Check 04: Mutations
```jsx
const mutation = useMutation((data) => api.post("/items", data));
mutation.mutate({ name: "test" });
```
<details><summary>Answer</summary>
`mutate` triggers the mutation. `mutation.isLoading`, `mutation.isSuccess`, `mutation.error` track status. Use `onSuccess` callback for side effects.
</details>

## Check 05: Invalidation
```jsx
queryClient.invalidateQueries(["items"]);
```
<details><summary>Answer</summary>
Marks queries matching key as stale. Active queries refetch immediately. Inactive queries refetch on next mount.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Missing Query Key
```jsx
useQuery(() => fetch("/api/data"));
```
<details><summary>Answer</summary>
**Bug:** First argument must be a query key (array). Without it, caching doesn't work.
**Fix:** `useQuery(["data"], () => fetch("/api/data").then(r => r.json()));`.
</details>

## Debug 02 (Medium): Query Key Not Unique
```jsx
useQuery(["user"], () => fetch(`/api/users/${userId}`));
```
<details><summary>Answer</summary>
**Bug:** Query key is "user" for all users. Changing userId doesn't refetch (same key).
**Fix:** `useQuery(["user", userId], () => fetch(...));` — include userId in key.
</details>

## Debug 03 (Hard): Mutation Without Invalidation
```jsx
const mutation = useMutation((data) => postData(data));
// after mutation, list is stale but not refetched
```
<details><summary>Answer</summary>
**Bug:** No cache invalidation after mutation. UI shows stale data.
**Fix:** `onSuccess: () => queryClient.invalidateQueries(["items"])`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Non-unique query keys
```jsx
// WRONG — same key for different data
useQuery(["data"], () => fetch(`/api/${id}`));
// CORRECT — include variables
useQuery(["data", id], () => fetch(`/api/${id}`));
```

## Mistake 02: No invalidation after mutation
```jsx
// WRONG — stale UI
const m = useMutation(addItem);
m.mutate(data);
// CORRECT
const m = useMutation(addItem, {
  onSuccess: () => queryClient.invalidateQueries(["items"])
});
```

## Mistake 03: Not using isLoading vs isFetching
```jsx
// isLoading — no data yet (first load)
// isFetching — fetching (including background refetch)
if (isLoading) return <Spinner />;
```

## Mistake 04: Fetching in useEffect
```jsx
// WRONG — reinvent React Query
useEffect(() => { fetch().then(setData); }, []);
// CORRECT — let React Query handle it
const { data } = useQuery(["key"], fetch);
```

## Mistake 05: Not handling errors
```jsx
// WRONG — silent failure
const { data } = useQuery(...);
// CORRECT
const { data, error } = useQuery(...);
if (error) return <Error />;
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual Fetch State
### Before
```jsx
const [data, setData] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);
useEffect(() => {
  fetch(url).then(r => r.json()).then(setData).catch(setError).finally(() => setLoading(false));
}, [url]);
```
### After
```jsx
const { data, loading, error } = useQuery(["key", url], () => fetch(url).then(r => r.json()));
```

## Refactor 02 (Medium): No Cache Key
### Before
```jsx
useQuery(["users"], fetchUsers);
useQuery(["users"], fetchUsers); // duplicate
```
### After
```jsx
// Same key = shared cache
useQuery(["users"], fetchUsers); // both components share
```

## Refactor 03 (Hard): Manual Mutation
### Before
```jsx
async function addUser(user) {
  await api.post("/users", user);
  const users = await api.get("/users");
  setUsers(users);
}
```
### After
```jsx
const mutation = useMutation((user) => api.post("/users", user), {
  onSuccess: () => queryClient.invalidateQueries(["users"]),
});
```

---

## Approach Comparison — different ways to solve it

## Problem: Data Fetching

### Approach 1: useEffect + useState
```jsx
const [data, setData] = useState();
const [loading, setLoading] = useState(true);
useEffect(() => {
  fetch(url).then(r => r.json()).then(setData).finally(() => setLoading(false));
}, [url]);
```

### Approach 2: React Query
```jsx
const { data, isLoading } = useQuery(["data", url], () => fetch(url).then(r => r.json()));
```

**Winner:** Approach 2 — caching, refetching, loading states, error handling all built in.

---

## Problem: Optimistic Update

### Approach 1: Manual
```jsx
// Complex state management
```

### Approach 2: React Query onMutate
```jsx
useMutation(updateItem, {
  onMutate: async (newItem) => {
    await queryClient.cancelQueries(["items"]);
    const prev = queryClient.getQueryData(["items"]);
    queryClient.setQueryData(["items"], (old) => [...old, newItem]);
    return { prev };
  },
  onError: (_e, _v, ctx) => queryClient.setQueryData(["items"], ctx.prev),
});
```

**Winner:** Approach 2 — built-in optimistic update pattern.
