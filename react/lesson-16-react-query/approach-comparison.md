# Lesson 16 — Approach Comparison

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
