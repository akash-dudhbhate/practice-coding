# Lesson 16 — Debug Exercises

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
