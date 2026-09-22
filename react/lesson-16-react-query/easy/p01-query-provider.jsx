/*
LESSON 16 — React Query
EASY P01 — QueryClientProvider + First useQuery
============================================
CONCEPT: React Query manages server state (fetching, caching, revalidation) for you. `QueryClientProvider` makes a `QueryClient` available to the tree; `useQuery({queryKey, queryFn})` fetches and caches by key.
PROBLEM: Create `const queryClient = new QueryClient()`. Build `UserList` calling `useQuery` with `queryKey: ["users"]` and a `queryFn` fetching jsonplaceholder `/users`; render Loading while `isLoading`, `error.message` on `error`, else a `<ul>` of names keyed by `u.id`. `App` wraps `UserList` in `<QueryClientProvider client={queryClient}>`.
TRY THIS: Render `<App />` — watch the Loading state flip into the user list.
EXPECTED OUTPUT: "Loading..." then a list of user names from the API.
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
