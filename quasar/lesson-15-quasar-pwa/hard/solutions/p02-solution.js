// Complete offline data sync system
// Stores API requests while offline, replays when back online, handles conflicts.

const SYNC_QUEUE_KEY = 'offline_sync_queue'

// --- Queue management ---
function getQueue() {
  const data = localStorage.getItem(SYNC_QUEUE_KEY)
  return data ? JSON.parse(data) : []
}

function saveQueue(queue) {
  localStorage.setItem(SYNC_QUEUE_KEY, JSON.stringify(queue))
}

function addToQueue(method, url, body = null) {
  const queue = getQueue()
  queue.push({
    id: Date.now() + Math.random(),
    method,
    url,
    body,
    timestamp: new Date().toISOString(),
  })
  saveQueue(queue)
  console.log(`[Sync] Queued: ${method} ${url}`)
}

// --- Wrapper around fetch that queues when offline ---
async function smartFetch(url, options = {}) {
  if (!navigator.onLine) {
    addToQueue(options.method || 'GET', url, options.body)
    return { offline: true, message: 'Request queued for sync' }
  }
  return fetch(url, options)
}

// --- Replay queued requests when back online ---
async function syncQueue() {
  const queue = getQueue()
  if (queue.length === 0) return { synced: 0, conflicts: [] }

  const results = { synced: 0, conflicts: [] }

  for (const item of queue) {
    try {
      const res = await fetch(item.url, {
        method: item.method,
        headers: { 'Content-Type': 'application/json' },
        body: item.body,
      })

      if (res.status === 409) {
        // Conflict — server has a newer version
        results.conflicts.push({ item, serverData: await res.json() })
      } else if (res.ok) {
        results.synced++
      }
    } catch (e) {
      console.error(`[Sync] Failed to replay: ${item.method} ${item.url}`, e)
      // Keep in queue if network error
      break
    }
  }

  // Remove successfully synced items
  const remaining = getQueue().slice(results.synced)
  saveQueue(remaining)

  console.log(`[Sync] Synced ${results.synced} requests, ${results.conflicts.length} conflicts`)
  return results
}

// --- Setup online/offline listeners ---
function setupSync() {
  window.addEventListener('online', async () => {
    console.log('[Sync] Back online — starting sync...')
    const result = await syncQueue()
    if (result.synced > 0) {
      console.log(`[Sync] ${result.synced} requests synced successfully`)
    }
    if (result.conflicts.length > 0) {
      console.warn(`[Sync] ${result.conflicts.length} conflicts detected`)
    }
  })

  window.addEventListener('offline', () => {
    console.log('[Sync] Gone offline — requests will be queued')
  })
}

// --- Export ---
export { smartFetch, syncQueue, setupSync, getQueue }

// Example usage:
// setupSync()
// await smartFetch('/api/users', { method: 'POST', body: JSON.stringify({ name: 'Alice' }) })
