<!--
  Offline-First Mobile App
  ------------------------
  - Caches data using Capacitor Storage (localStorage fallback on web)
  - Detects online/offline status and shows a banner when offline
  - Automatically syncs cached data when the connection is restored
  - Provides pull-to-refresh (v-touch-pull) to manually refetch data
  - Fires haptic feedback on sync success / failure (mobile only)
-->
<template>
  <q-page class="q-pa-md">
    <!-- Offline banner -->
    <q-banner
      v-if="!isOnline"
      class="bg-orange-2 text-orange-9 q-mb-md"
      dense
    >
      <template #avatar>
        <q-icon name="cloud_off" />
      </template>
      You are offline. Data will sync when the connection returns.
    </q-banner>

    <!-- Pull-to-refresh wrapper -->
    <div
      v-touch-pull="onPull"
      class="pull-container"
    >
      <!-- Refresh indicator shown while pulling / loading -->
      <div v-if="refreshing" class="column flex-center q-py-sm">
        <q-spinner color="primary" size="32px" />
        <span class="text-caption text-grey-7">Refreshing…</span>
      </div>

      <!-- Data list -->
      <q-list bordered separator>
        <q-item v-for="item in items" :key="item.id">
          <q-item-section>
            <q-item-label>{{ item.title }}</q-item-label>
            <q-item-label caption>{{ item.body }}</q-item-label>
          </q-item-section>
          <q-item-section side>
            <q-badge
              :color="item.synced ? 'green' : 'orange'"
              :label="item.synced ? 'synced' : 'pending'"
            />
          </q-item-section>
        </q-item>
      </q-list>

      <!-- Add new item (works offline) -->
      <div class="row q-mt-md q-gutter-sm">
        <q-input
          v-model="newItemTitle"
          outlined
          dense
          label="New item"
          class="col"
          @keyup.enter="addItem"
        />
        <q-btn color="primary" icon="add" label="Add" @click="addItem" />
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// ---- State ---------------------------------------------------------------
const items = ref([])
const isOnline = ref(navigator.onLine)
const refreshing = ref(false)
const newItemTitle = ref('')

// Storage abstraction — uses Capacitor Storage on mobile, localStorage on web
let storageGet, storageSet

// ---- Lifecycle -----------------------------------------------------------
onMounted(async () => {
  await initStorage()
  await loadCached()

  window.addEventListener('online', onOnline)
  window.addEventListener('offline', onOffline)

  if (isOnline.value) await fetchItems()
})

onUnmounted(() => {
  window.removeEventListener('online', onOnline)
  window.removeEventListener('offline', onOffline)
})

// ---- Storage init --------------------------------------------------------
async function initStorage() {
  if ($q.platform.is.capacitor) {
    const { Storage } = await import('@capacitor/storage')
    storageGet = (key) => Storage.get({ key }).then((r) => r.value)
    storageSet = (key, value) => Storage.set({ key, value })
  } else {
    storageGet = (key) => Promise.resolve(localStorage.getItem(key))
    storageSet = (key, value) => Promise.resolve(localStorage.setItem(key, value))
  }
}

// ---- Data loading --------------------------------------------------------
async function loadCached() {
  const cached = await storageGet('cached_items')
  if (cached) {
    items.value = JSON.parse(cached)
  }
}

async function persistCache() {
  await storageSet('cached_items', JSON.stringify(items.value))
}

/**
 * Simulate an API fetch. In a real app this would call your backend.
 */
async function fetchItems() {
  refreshing.value = true
  try {
    // Simulated network delay
    await new Promise((r) => setTimeout(r, 800))

    // If we already have items, mark them all as synced
    items.value = items.value.map((i) => ({ ...i, synced: true }))
    await persistCache()
    haptic('success')
  } catch {
    haptic('error')
    $q.notify({ type: 'negative', message: 'Fetch failed' })
  } finally {
    refreshing.value = false
  }
}

// ---- Online / offline handlers ------------------------------------------
function onOnline() {
  isOnline.value = true
  $q.notify({ type: 'positive', message: 'Back online — syncing…' })
  syncPending()
}

function onOffline() {
  isOnline.value = false
  $q.notify({ type: 'warning', message: 'Gone offline' })
}

/**
 * Sync all unsynced items when connectivity returns.
 */
async function syncPending() {
  const hasPending = items.value.some((i) => !i.synced)
  if (hasPending) {
    await fetchItems()
  }
}

// ---- Pull-to-refresh -----------------------------------------------------
function onPull({ pullAmount, ease }) {
  // Quasar calls this continuously while pulling; trigger refresh
  // once the pull distance exceeds a threshold.
  if (pullAmount > 80 && !refreshing.value) {
    fetchItems()
  }
}

// ---- Add item (offline-capable) -----------------------------------------
async function addItem() {
  if (!newItemTitle.value.trim()) return

  items.value.push({
    id: Date.now(),
    title: newItemTitle.value,
    body: isOnline.value ? 'Added online' : 'Added offline',
    synced: isOnline.value,
  })
  newItemTitle.value = ''
  await persistCache()

  if (isOnline.value) await fetchItems()
  haptic('light')
}

// ---- Haptics -------------------------------------------------------------
async function haptic(type) {
  if (!$q.platform.is.capacitor) return
  try {
    const { Haptics, NotificationType, ImpactStyle } = await import('@capacitor/haptics')
    if (type === 'success') await Haptics.notification({ type: NotificationType.Success })
    else if (type === 'error') await Haptics.notification({ type: NotificationType.Error })
    else await Haptics.impact({ style: ImpactStyle.Light })
  } catch {
    // ignore
  }
}
</script>

<style scoped>
.pull-container {
  min-height: 200px;
  touch-action: pan-y;
}
</style>
