<!--
  Lesson 14 - Easy - P01: Notification Types
  4 buttons showing different notification types (positive, negative,
  warning, info) with custom message, icon, and position for each.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Notification Types</div>

    <div class="q-gutter-md">
      <q-btn color="positive" icon="check_circle" label="Success" no-caps @click="showPositive" />
      <q-btn color="negative" icon="error" label="Error" no-caps @click="showNegative" />
      <q-btn color="warning" icon="warning" label="Warning" no-caps @click="showWarning" />
      <q-btn color="info" icon="info" label="Info" no-caps @click="showInfo" />
    </div>
  </q-page>
</template>

<script setup>
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Positive notification — top-right position
function showPositive() {
  $q.notify({
    type: 'positive',
    message: 'Operation completed successfully!',
    icon: 'check_circle',
    position: 'top-right',
    timeout: 3000,
  })
}

// Negative notification — bottom-right position
function showNegative() {
  $q.notify({
    type: 'negative',
    message: 'An error occurred. Please try again.',
    icon: 'error',
    position: 'bottom-right',
    timeout: 3000,
  })
}

// Warning notification — top position (centered)
function showWarning() {
  $q.notify({
    type: 'warning',
    message: 'This action may have consequences.',
    icon: 'warning',
    position: 'top',
    timeout: 3000,
  })
}

// Info notification — bottom position (centered)
function showInfo() {
  $q.notify({
    type: 'info',
    message: 'Here is some useful information.',
    icon: 'info',
    position: 'bottom',
    timeout: 3000,
  })
}
</script>

<style scoped>
</style>
