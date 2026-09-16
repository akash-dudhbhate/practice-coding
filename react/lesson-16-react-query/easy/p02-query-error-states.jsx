/*
LESSON 16 — React Query
EASY P02 — Loading / Error / Success States
============================================
CONCEPT: `useQuery` hands you `isLoading`, `error`, `data`, and `refetch` — no manual try/catch in the component. Rendering all three states explicitly is the core React Query skill.
PROBLEM: Write `fetchWithError` — an async function that throws `"Random API failure"` ~50% of the time, else fetches user 1 from jsonplaceholder. Build `UserWithErrors` using `useQuery({queryKey: ["user-random"], queryFn: fetchWithError})`: Loading state, a red error message with a Retry button calling `refetch()`, and success showing `data.name` with a Refetch button.
TRY THIS: Render `<UserWithErrors />` and hit Refetch until you see the random error, then Retry.
EXPECTED OUTPUT: Alternates between the name and "Error: Random API failure" with working Retry.
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
