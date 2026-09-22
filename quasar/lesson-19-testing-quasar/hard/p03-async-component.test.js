/**
 * LESSON 19 — Testing Quasar Apps
 * HARD P03 — Async Component Tests
 * ============================================
 * CONCEPT: For components that fetch on mount: mock global.fetch per
 * test; a never-resolving Promise pins the loading state; flushPromises()
 * lets the fetch + re-render settle; a refetch button asserts fetch was
 * called again.
 *
 * PROBLEM: Test an inline async component (fetchData() in mounted,
 * loading/error/data refs, refetch button): loading shows first, data
 * renders after a mocked success, an !ok response shows the error state,
 * and clicking refetch issues a second fetch with new data.
 *
 * TRY THIS: global.fetch.mockReturnValueOnce(new Promise(() => {}))
 * const w = mount(Comp); expect(w.find('[data-test="loading"]').exists()).toBe(true)
 * await flushPromises()
 *
 * EXPECTED OUTPUT: Four its — loading, success, error, refetch.
 *
 * CHECK: python3 check.py hard/p03
 */
// TODO: write your async component tests here
