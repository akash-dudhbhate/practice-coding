/*
LESSON 16 — React Query
EASY P03 — Dynamic Query Keys + Caching
============================================
CONCEPT: Putting a variable in the `queryKey` (like `["user", userId]`) gives each id its own cache entry — switching back to a visited id renders instantly from cache with no refetch.
PROBLEM: Build `UserById({userId})` using `useQuery` with `queryKey: ["user", userId]` and a `queryFn` fetching `/users/${userId}`; show Loading then `data.name` + `data.email`. `App` holds `userId` in `useState(1)` with three buttons setting it to 1/2/3.
TRY THIS: Render `<App />`, click User 2 then back to User 1 — the return visit shows instantly (cached).
EXPECTED OUTPUT: Each id fetches once; revisiting an id skips the Loading state entirely.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
