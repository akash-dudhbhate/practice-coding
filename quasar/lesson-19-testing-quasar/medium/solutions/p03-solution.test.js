// Tests for API service (mock fetch)
// Run: vitest run medium/p03-solution.test.js
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest'

// --- API service (inline for self-contained test) ---
const apiService = {
  baseURL: 'https://api.example.com',

  async getUsers() {
    const res = await fetch(`${this.baseURL}/users`)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    return res.json()
  },

  async createUser(data) {
    const res = await fetch(`${this.baseURL}/users`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    return res.json()
  },
}

// --- Tests ---
describe('apiService', () => {
  const mockUsers = [{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }]

  beforeEach(() => {
    global.fetch = vi.fn()
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  it('getUsers returns data on success', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockUsers,
    })

    const users = await apiService.getUsers()
    expect(users).toEqual(mockUsers)
    expect(global.fetch).toHaveBeenCalledWith('https://api.example.com/users')
  })

  it('createUser sends correct payload', async () => {
    const newUser = { name: 'Charlie', email: 'charlie@test.com' }
    global.fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ id: 3, ...newUser }),
    })

    const result = await apiService.createUser(newUser)
    expect(result).toEqual({ id: 3, ...newUser })
    expect(global.fetch).toHaveBeenCalledWith(
      'https://api.example.com/users',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify(newUser),
      })
    )
  })

  it('throws error on 500 response', async () => {
    global.fetch.mockResolvedValueOnce({
      ok: false,
      status: 500,
      json: async () => ({ error: 'Server error' }),
    })

    await expect(apiService.getUsers()).rejects.toThrow('HTTP 500')
  })
})
