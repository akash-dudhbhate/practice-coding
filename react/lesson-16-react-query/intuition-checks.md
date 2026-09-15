# Lesson 16 — Intuition Checks

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
