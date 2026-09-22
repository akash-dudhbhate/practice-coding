/**
 * LESSON 19 — Testing Quasar Apps
 * MEDIUM P03 — API Service Test (mock fetch)
 * ============================================
 * CONCEPT: Replace global.fetch with vi.fn() in beforeEach, queue fake
 * responses with mockResolvedValueOnce, assert calls with
 * toHaveBeenCalledWith / expect.objectContaining, and rejections with
 * await expect(...).rejects.toThrow. Restore mocks in afterEach.
 *
 * PROBLEM: Test an inline apiService {getUsers, createUser}: getUsers
 * returns data and fetches the right URL; createUser POSTs the JSON
 * payload; a 500 response rejects with 'HTTP 500'.
 *
 * TRY THIS: global.fetch = vi.fn()
 * global.fetch.mockResolvedValueOnce({ ok: true, json: async () => users })
 * expect(global.fetch).toHaveBeenCalledWith('https://api.example.com/users')
 *
 * EXPECTED OUTPUT: Three its — GET data, POST payload, error on 500.
 *
 * CHECK: python3 check.py medium/p03
 */
// TODO: write your API service tests here
