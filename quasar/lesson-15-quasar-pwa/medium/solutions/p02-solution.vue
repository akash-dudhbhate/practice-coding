<template>
  <div>
    <q-banner v-if="!isOnline" class="bg-negative text-white">
      <q-icon name="wifi_off" class="q-mr-sm" />
      You are offline. Some features may be unavailable.
    </q-banner>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()
const isOnline = ref(navigator.onLine)

function onOnline() {
  isOnline.value = true
  $q.notify({ type: 'positive', message: 'Back online!', timeout: 3000 })
}

function onOffline() {
  isOnline.value = false
}

onMounted(() => {
  window.addEventListener('online', onOnline)
  window.addEventListener('offline', onOffline)
})

onUnmounted(() => {
  window.removeEventListener('online', onOnline)
  window.removeEventListener('offline', onOffline)
})
</script>
