/**
 * LESSON 15 — Quasar PWA
 * HARD P02 — Offline Sync Queue
 * ============================================
 * CONCEPT: While offline, queue API requests (method, url, body, timestamp)
 * in localStorage. On the 'online' event, replay them in order; HTTP 409
 * means a conflict — collect it separately instead of failing.
 *
 * PROBLEM: Export `smartFetch` (queues when !navigator.onLine, fetches
 * otherwise), `syncQueue` (replays the queue, returns { synced, conflicts }
 * and keeps failed items), `setupSync` (wires online/offline listeners),
 * and `getQueue`. Persist the queue under a storage key.
 *
 * TRY THIS: if (!navigator.onLine) { addToQueue(method, url, body); return { offline: true } }
 * In syncQueue: res.status === 409 → conflicts.push(...); res.ok → synced++
 *
 * EXPECTED OUTPUT: Offline writes are stored; reconnecting replays them and
 * reports how many synced vs. conflicted.
 *
 * CHECK: python3 check.py hard/p02
 */
// TODO: write your sync system here
