<template>
  <div class="q-pa-md">
    <q-btn
      v-if="canInstall"
      label="Install App"
      icon="download"
      color="primary"
      @click="install"
    />
    <q-banner v-if="installed" class="bg-positive text-white q-mt-sm">
      App installed successfully!
    </q-banner>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const canInstall = ref(false)
const installed = ref(false)
let deferredPrompt = null

function onBeforeInstallPrompt(e) {
  // Prevent the default browser prompt
  e.preventDefault()
  deferredPrompt = e
  canInstall.value = true
}

async function install() {
  if (!deferredPrompt) return
  deferredPrompt.prompt()
  const { outcome } = await deferredPrompt.userChoice
  if (outcome === 'accepted') {
    installed.value = true
    canInstall.value = false
  } else {
    canInstall.value = false
  }
  deferredPrompt = null
}

onMounted(() => {
  window.addEventListener('beforeinstallprompt', onBeforeInstallPrompt)
  window.addEventListener('appinstalled', () => { installed.value = true; canInstall.value = false })
})

onUnmounted(() => {
  window.removeEventListener('beforeinstallprompt', onBeforeInstallPrompt)
})
</script>
