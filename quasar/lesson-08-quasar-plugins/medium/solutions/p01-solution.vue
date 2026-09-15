<template>
  <!-- Delete confirmation flow using $q.dialog -->
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Delete Confirmation</div>
    <q-card class="q-pa-lg">
      <q-card-section>
        <p>Click the button below to trigger a delete confirmation dialog.</p>
        <q-btn label="Delete Item" color="negative" icon="delete" @click="confirmDelete" />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Show confirmation dialog before deleting
function confirmDelete() {
  $q.dialog({
    title: 'Confirm Delete',
    message: 'Are you sure you want to delete this item? This action cannot be undone.',
    cancel: true,
    persistent: true,
    ok: { label: 'Delete', color: 'negative' },
    cancel: { label: 'Cancel', color: 'grey' },
  }).onOk(() => {
    // User confirmed - show "deleted" notification
    $q.notify({ type: 'positive', message: 'Item deleted successfully!' })
  }).onCancel(() => {
    // User cancelled - show "cancelled" notification
    $q.notify({ type: 'info', message: 'Delete cancelled.' })
  })
}
</script>

<style scoped>
.q-card {
  max-width: 500px;
  margin: 0 auto;
}
</style>
