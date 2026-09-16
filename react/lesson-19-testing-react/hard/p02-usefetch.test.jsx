/*
LESSON 19 — Testing React
HARD P02 — Test a useFetch Hook with renderHook
============================================
CONCEPT: `renderHook(() => useFetch(url))` runs a hook in isolation and exposes `result.current` — re-read it after `waitFor` to see state updates. `rerender` with new props tests reactive behavior like refetching on url change.
PROBLEM: For `useFetch` (import from "../useFetch") returning `{data, loading, error}`, write FOUR tests with `fetch` mocked via `jest.spyOn`: (1) initial `result.current.loading` is true, data null; (2) after `mockResolvedValue` + `waitFor`, `data` equals `{name: "Alice"}`; (3) `mockRejectedValue` → `error` is "Failed"; (4) `renderHook` with `initialProps: {url}` + `rerender({url: ".../v2"})` refetches and `data` becomes `{name: "Charlie"}`. Add `afterEach` restore.
TRY THIS: Run the suite — hook lifecycle (loading → data → error → refetch) fully covered.
EXPECTED OUTPUT: 4 passing tests for the hook's states and refetch behavior.
CHECK: python3 check.py hard/p02
*/
// TODO: write your test from scratch
