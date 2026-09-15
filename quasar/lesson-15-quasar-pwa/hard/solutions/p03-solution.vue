<template>
  <div class="q-pa-md">
    <q-card class="q-mb-md">
      <q-card-section>
        <div class="text-h6">PWA Settings</div>
      </q-card-section>

      <!-- Install status -->
      <q-item>
        <q-item-section avatar><q-icon :name="isInstalled ? 'check_circle' : 'cancel'" :color="isInstalled ? 'positive' : 'grey'" /></q-item-section>
        <q-item-section>
          <q-item-label>Install Status</q-item-label>
          <q-item-label caption>{{ isInstalled ? 'Installed as PWA' : 'Running in browser' }}</q-item-label>
        </q-item-section>
      </q-item>

      <!-- Update available -->
      <q-item v-if="updateAvailable">
        <q-item-section avatar><q-icon name="system_update" color="warning" /></q-item-section>
        <q-item-section>
          <q-item-label>Update Available</q-item-label>
          <q-item-label caption>A new version is ready</q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-btn label="Refresh" color="primary" size="sm" @click="applyUpdate" />
        </q-item-section>
      </q-item>

      <q-separator />

      <!-- Push notification toggle -->
      <q-item>
        <q-item-section avatar><q-icon name="notifications" /></q-item-section>
        <q-item-section>
          <q-item-label>Push Notifications</q-item-label>
          <q-item-label caption>{{ pushPermission }}</q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-toggle v-model="pushEnabled" @update:model-value="togglePush" />
        </q-item-section>
      </q-item>

      <q-separator />

      <!-- Offline storage usage -->
      <q-item>
        <q-item-section avatar><q-icon name="storage" /></q-item-section>
        <q-item-section>
          <q-item-label>Storage Usage</q-item-label>
          <q-item-label caption>{{ storageUsage }}</q-item-label>
        </q-item-section>
      </q-item>

      <q-card-actions align="right">
        <q-btn label="Clear Cache" color="negative" flat @click="clearCache" />
      </q-card-actions>
    </q-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()
const isInstalled = ref(false)
const updateAvailable = ref(false)
const pushEnabled = ref(false)
const pushPermission = ref('default')
const storageUsage = ref('Calculating...')
let swRegistration = null

onMounted(async () => {
  // Check install status
  isInstalled.value = window.matchMedia('(display-mode: standalone)').matches

  // Check push permission
  if ('Notification' in window) {
    pushPermission.value = Notification.permission
    pushEnabled.value = Notification.permission === 'granted'
  }

  // Load persisted settings
  const settings = JSON.parse(localStorage.getItem('pwa_settings') || '{}')
  pushEnabled.value = settings.pushEnabled ?? pushEnabled.value

  // Check for service worker updates
  if ('serviceWorker' in navigator) {
    swRegistration = await navigator.serviceWorker.getRegistration()
    if (swRegistration) {
      swRegistration.addEventListener('updatefound', () => {
        updateAvailable.value = true
      })
    }
  }

  // Calculate storage usage
  if (navigator.storage?.estimate) {
    const { usage, quota } = await navigator.storage.estimate()
    storageUsage.value = `${(usage / 1024 / 1024).toFixed(1)} MB / ${(quota / 1024 / 1024).toFixed(0)} MB`
  } else {
    storageUsage.value = 'Not available'
  }
})

function persistSettings() {
  localStorage.setItem('pwa_settings', JSON.stringify({ pushEnabled: pushEnabled.value }))
}

async function togglePush(val) {
  if (val) {
    if ('Notification' in window) {
      const result = await Notification.requestPermission()
      pushPermission.value = result
      pushEnabled.value = result === 'granted'
      if (result !== 'granted') {
        $q.notify({ type: 'negative', message: 'Push permission denied' })
      }
    }
  } else {
    pushEnabled.value = false
  }
  persistSettings()
}

function applyUpdate() {
  if (swRegistration?.waiting) {
    swRegistration.waiting.postMessage({ type: 'SKIP_WAITING' })
  }
  window.location.reload()
}

async function clearCache() {
  $q.dialog({
    title: 'Clear Cache',
    message: 'This will remove all cached data. Continue?',
    cancel: true,
  }).onOk(async () => {
    if ('caches' in window) {
      const keys = await caches.keys()
      await Promise.all(keys.map(k => caches.delete(k)))
    }
    localStorage.removeItem('offline_sync_queue')
    $q.notify({ type: 'positive', message: 'Cache cleared' })
    // Recalculate storage
    if (navigator.storage?.estimate) {
      const { usage } = await navigator.storage.estimate()
      storageUsage.value = `${(usage / 1024 / 1024).toFixed(1)} MB`
    }
  })
}
</script>
