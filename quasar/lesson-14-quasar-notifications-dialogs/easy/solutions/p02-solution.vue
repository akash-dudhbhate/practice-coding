<!--
  Lesson 14 - Easy - P02: Delete Confirmation Flow
  Button opens a confirm dialog. Confirm triggers a "deleted" notification
  with an Undo action (5s timeout). Cancel shows a "cancelled" notification.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Delete Confirmation Flow</div>

    <q-btn color="negative" icon="delete" label="Delete Item" no-caps @click="confirmDelete" />
  </q-page>
</template>

<script setup>
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Open confirmation dialog
function confirmDelete() {
  $q.dialog({
    title: 'Confirm Delete',
    message: 'Are you sure you want to delete this item? This action can be undone.',
    cancel: true,
    persistent: true,
    ok: { label: 'Delete', color: 'negative', unelevated: true },
    cancel: { label: 'Cancel', color: 'grey', flat: true },
  }).onOk(() => {
    // User confirmed — show "deleted" notification with Undo action
    $q.notify({
      type: 'positive',
      message: 'Item deleted successfully.',
      icon: 'delete',
      timeout: 5000, // 5 seconds to undo
      actions: [
        {
          label: 'Undo',
          color: 'white',
          handler: () => {
            $q.notify({ type: 'info', message: 'Deletion undone. Item restored.', timeout: 2000 })
          },
        },
      ],
    })
  }).onCancel(() => {
    // User cancelled — show "cancelled" notification
    $q.notify({
      type: 'info',
      message: 'Deletion cancelled.',
      icon: 'cancel',
      timeout: 2000,
    })
  })
}
</script>

<style scoped>
</style>
