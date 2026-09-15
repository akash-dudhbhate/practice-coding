<template>
  <div class="q-pa-md">
    <q-btn label="Enter Your Name" color="primary" @click="openPrompt" />
  </div>
</template>

<script setup>
import { useQuasar } from 'quasar'

const $q = useQuasar()

function openPrompt() {
  $q.dialog({
    title: 'Enter Your Name',
    message: 'Please enter your name:',
    prompt: {
      model: '',
      type: 'text',
      isValid: (val) => val.trim().length > 0,
    },
    cancel: true,
    persistent: true,
  }).onOk((name) => {
    $q.notify({
      type: 'positive',
      message: `You entered: ${name}`,
      position: 'top',
    })
  }).onCancel(() => {
    $q.notify({ type: 'info', message: 'Prompt cancelled' })
  })
}
</script>
