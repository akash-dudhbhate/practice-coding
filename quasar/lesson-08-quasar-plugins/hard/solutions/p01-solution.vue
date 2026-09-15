<template>
  <!-- Notification system: composable useNotifications wrapping $q.notify with presets -->
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Notification System</div>
    <div class="row q-gutter-md">
      <q-btn label="Success" color="positive" @click="notify.success('Operation completed!')" />
      <q-btn label="Error" color="negative" @click="notify.error('Operation failed!')" />
      <q-btn label="Warning" color="warning" @click="notify.warning('Please check your input')" />
      <q-btn label="Info" color="info" @click="notify.info('Here is a tip')" />
      <q-btn label="Delete with Undo" color="negative" icon="delete" @click="notifyDeleteWithUndo" />
    </div>
  </q-page>
</template>

<script setup>
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Composable: useNotifications wraps $q.notify with presets
function useNotifications() {
  // Preset configurations with default colors, icons, and timeouts
  const presets = {
    success: { type: 'positive', icon: 'check_circle', timeout: 3000 },
    error: { type: 'negative', icon: 'error', timeout: 5000 },
    warning: { type: 'warning', icon: 'warning', timeout: 4000 },
    info: { type: 'info', icon: 'info', timeout: 3000 },
  }

  // Generic notify function that merges preset with custom message
  function notify(type, message, overrides = {}) {
    const preset = presets[type]
    if (!preset) {
      console.warn(`Unknown notification type: ${type}`)
      return
    }
    $q.notify({
      ...preset,
      message,
      ...overrides,
    })
  }

  return {
    success: (msg, overrides) => notify('success', msg, overrides),
    error: (msg, overrides) => notify('error', msg, overrides),
    warning: (msg, overrides) => notify('warning', msg, overrides),
    info: (msg, overrides) => notify('info', msg, overrides),
  }
}

// Initialize the composable
const notify = useNotifications()

// Delete notification with "Undo" action
function notifyDeleteWithUndo() {
  $q.notify({
    type: 'negative',
    message: 'Item deleted. Undo?',
    icon: 'delete',
    timeout: 5000,
    actions: [
      {
        label: 'Undo',
        color: 'white',
        handler: () => {
          $q.notify({ type: 'positive', message: 'Delete undone!' })
        },
      },
    ],
  })
}
</script>

<style scoped>
.q-page {
  max-width: 600px;
  margin: 0 auto;
}
</style>
