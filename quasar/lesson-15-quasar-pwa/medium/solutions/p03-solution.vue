<template>
  <div class="q-pa-md">
    <q-btn label="Enable Push Notifications" color="primary" @click="requestPermission" :disable="permission === 'granted'" />
    <p class="q-mt-sm">Status: <strong>{{ permission }}</strong></p>
    <q-btn v-if="permission === 'granted'" label="Send Test Notification" color="secondary" @click="sendTest" class="q-mt-sm" />
    <q-banner v-if="iosLimitation" class="bg-warning q-mt-sm">
      Note: iOS requires the app to be installed as a PWA for push notifications.
    </q-banner>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const permission = ref('default')
const iosLimitation = ref(false)

onMounted(() => {
  if ('Notification' in window) {
    permission.value = Notification.permission
  }
  // Detect iOS limitations
  const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent)
  const isStandalone = window.matchMedia('(display-mode: standalone)').matches
  if (isIOS && !isStandalone) {
    iosLimitation.value = true
  }
})

async function requestPermission() {
  if (!('Notification' in window)) {
    alert('Notifications not supported in this browser')
    return
  }
  const result = await Notification.requestPermission()
  permission.value = result
}

function sendTest() {
  new Notification('Test Notification', {
    body: 'Push notifications are working!',
    icon: '/icons/icon-128.png',
  })
}
</script>
