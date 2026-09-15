<template>
  <div class="q-pa-md">
    <q-banner :class="isPWA ? 'bg-positive text-white' : 'bg-info text-white'">
      <q-icon :name="isPWA ? 'install_mobile' : 'language'" class="q-mr-sm" />
      {{ isPWA ? 'Running as PWA (standalone mode)' : 'Running in browser' }}
    </q-banner>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isPWA = ref(false)

function checkStandalone() {
  // Check if running in standalone mode (PWA)
  if (typeof window !== 'undefined' && window.matchMedia) {
    isPWA.value = window.matchMedia('(display-mode: standalone)').matches
  }
}

onMounted(() => {
  checkStandalone()
  // Listen for display mode changes
  if (window.matchMedia) {
    window.matchMedia('(display-mode: standalone)').addEventListener('change', checkStandalone)
  }
})

onUnmounted(() => {
  if (window.matchMedia) {
    window.matchMedia('(display-mode: standalone)').removeEventListener('change', checkStandalone)
  }
})
</script>
