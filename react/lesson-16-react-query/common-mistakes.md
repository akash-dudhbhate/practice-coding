# Lesson 16 — Common Mistakes

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
