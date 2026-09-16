/*
LESSON 19 — Testing React
MEDIUM P03 — Test an Async Component (Mock fetch)
============================================
CONCEPT: Never hit the network in tests: `jest.spyOn(global, "fetch")` + `mockResolvedValue`/`mockRejectedValue`/`mockImplementation` control the response. `waitFor` (or `findBy`) pauses the assertion until the async UI updates.
PROBLEM: For `UserProfile` (import "../UserProfile") taking `userId`, mock `fetch` three ways across THREE tests: (1) a never-resolving promise → "loading" stays visible; (2) `mockResolvedValue` `{json: async () => ({id:1, name:"Alice"})}` → `await waitFor` until "Alice" appears; (3) `mockRejectedValue` → error text appears. Add `afterEach(() => jest.restoreAllMocks())`.
TRY THIS: Run the suite — all three async states verified without any real request.
EXPECTED OUTPUT: 3 passing tests: pending, resolved, and rejected fetch states.
CHECK: python3 check.py medium/p03
*/
// TODO: write your test from scratch
