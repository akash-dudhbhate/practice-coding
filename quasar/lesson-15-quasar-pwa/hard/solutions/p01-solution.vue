<template>
  <div class="q-pa-md">
    <q-banner v-if="!showOnboarding" class="bg-positive text-white">
      App is installed. Enjoy!
    </q-banner>

    <q-card v-if="showOnboarding" class="q-mb-md">
      <q-card-section>
        <div class="text-h6">Install My App</div>
        <p>Get the full experience by installing this app as a PWA:</p>
        <q-list>
          <q-item>
            <q-item-section avatar><q-icon name="wifi_off" color="primary" /></q-item-section>
            <q-item-section>Works offline — access content without internet</q-item-section>
          </q-item>
          <q-item>
            <q-item-section avatar><q-icon name="install_mobile" color="primary" /></q-item-section>
            <q-item-section>Installable — appears on your home screen</q-item-section>
          </q-item>
          <q-item>
            <q-item-section avatar><q-icon name="notifications" color="primary" /></q-item-section>
            <q-item-section>Push notifications — stay up to date</q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
      <q-card-actions align="right">
        <q-btn flat label="Maybe later" @click="dismiss" />
        <q-btn v-if="canInstall" label="Install" color="primary" @click="install" />
      </q-card-actions>
    </q-card>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const showOnboarding = ref(false)
const canInstall = ref(false)
const isInstalled = ref(false)
let deferredPrompt = null

function checkInstalled() {
  isInstalled.value = window.matchMedia('(display-mode: standalone)').matches
  const dismissed = localStorage.getItem('pwa_onboarding_dismissed')
  showOnboarding.value = !isInstalled.value && dismissed !== 'true'
}

function onBeforeInstallPrompt(e) {
  e.preventDefault()
  deferredPrompt = e
  canInstall.value = true
}

async function install() {
  if (!deferredPrompt) return
  deferredPrompt.prompt()
  await deferredPrompt.userChoice
  deferredPrompt = null
  canInstall.value = false
  showOnboarding.value = false
}

function dismiss() {
  showOnboarding.value = false
  localStorage.setItem('pwa_onboarding_dismissed', 'true')
}

onMounted(() => {
  checkInstalled()
  window.addEventListener('beforeinstallprompt', onBeforeInstallPrompt)
})

onUnmounted(() => {
  window.removeEventListener('beforeinstallprompt', onBeforeInstallPrompt)
})
</script>
