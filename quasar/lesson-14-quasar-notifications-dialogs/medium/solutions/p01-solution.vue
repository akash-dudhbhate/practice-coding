<template>
  <div class="q-pa-md">
    <q-btn label="Start Operation" color="primary" @click="startOperation" :disable="loading" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()
const loading = ref(false)

function startOperation() {
  loading.value = true
  // Persistent loading notification (timeout=0 means it stays until dismissed)
  const dismiss = $q.notify({
    message: 'Loading...',
    spinner: true,
    timeout: 0,
    position: 'center',
  })

  // Simulate 3-second operation
  setTimeout(() => {
    dismiss() // Dismiss the loading notification
    loading.value = false
    $q.notify({
      type: 'positive',
      message: 'Operation completed successfully!',
      timeout: 3000,
      position: 'top',
    })
  }, 3000)
}
</script>
