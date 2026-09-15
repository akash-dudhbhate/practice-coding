<template>
  <!-- Button showing notifications using $q.notify - 4 types -->
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Notification Types</div>
    <div class="row q-gutter-md">
      <q-btn label="Positive" color="positive" icon="check_circle" @click="notifyPositive" />
      <q-btn label="Negative" color="negative" icon="error" @click="notifyNegative" />
      <q-btn label="Warning" color="warning" icon="warning" @click="notifyWarning" />
      <q-btn label="Info" color="info" icon="info" @click="notifyInfo" />
    </div>
  </q-page>
</template>

<script setup>
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Positive notification (success)
function notifyPositive() {
  $q.notify({ type: 'positive', message: 'Operation successful!', timeout: 3000 })
}

// Negative notification (error)
function notifyNegative() {
  $q.notify({ type: 'negative', message: 'Something went wrong!', timeout: 3000 })
}

// Warning notification
function notifyWarning() {
  $q.notify({ type: 'warning', message: 'Please be careful!', timeout: 3000 })
}

// Info notification
function notifyInfo() {
  $q.notify({ type: 'info', message: 'Here is some information.', timeout: 3000 })
}
</script>

<style scoped>
.q-page {
  max-width: 600px;
  margin: 0 auto;
}
</style>
