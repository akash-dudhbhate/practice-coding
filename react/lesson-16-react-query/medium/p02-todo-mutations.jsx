/*
LESSON 16 — React Query
MEDIUM P02 — Todo App: One Query, Three Mutations
============================================
CONCEPT: Each CRUD operation is its own `useMutation` (add → POST, toggle → PATCH, delete → DELETE), and each invalidates the same `["todos"]` key so the UI always resyncs from the server.
PROBLEM: Build `TodoApp`: `useQuery(["todos"])` fetching 5 todos (default `[]`); `addMutation` (POST), `toggleMutation` (PATCH `{completed: true}`), `deleteMutation` (DELETE) — every `onSuccess` calls `qc.invalidateQueries({queryKey: ["todos"]})`. Render a controlled input + Add button, and a `<ul>` where each item shows ✓ when completed plus Toggle and Delete buttons calling `mutate(t.id)`.
TRY THIS: Render `<TodoApp />`, add a todo, toggle one, delete one — each action triggers a refetch.
EXPECTED OUTPUT: List updates after every mutation; ✓ appears on toggled items.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
