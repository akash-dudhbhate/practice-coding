/*
LESSON 16 — React Query
HARD P02 — Optimistic Updates
============================================
CONCEPT: Don't wait for the server: `onMutate` snapshots the cache (`getQueryData`), writes the new item instantly (`setQueryData`), and returns the snapshot as context. `onError` restores it (rollback); `onSettled` invalidates to resync either way.
PROBLEM: Build `OptimisticTodos`: `useQuery(["todos-optimistic"])`; a `simulateError` checkbox state; `addMutation` whose `mutationFn` throws when `simulateError` else POSTs. In `onMutate`: `await qc.cancelQueries`, snapshot `prev = qc.getQueryData`, `qc.setQueryData` appending the new todo, return `{prev}`. `onError` restores `context.prev`; `onSettled` invalidates. Render the checkbox, an Add Todo button, and the `<ul>`.
TRY THIS: Render `<OptimisticTodos />`, add a todo (appears instantly), then enable Simulate Error and add again — it appears then rolls back.
EXPECTED OUTPUT: Instant adds; with Simulate Error the item vanishes after the failed mutation.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
