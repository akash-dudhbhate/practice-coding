<template>
  <div class="q-pa-md">
    <q-btn label="Open Bottom Sheet" color="primary" @click="openBottomSheet" />
  </div>
</template>

<script setup>
import { useQuasar } from 'quasar'

const $q = useQuasar()

function openBottomSheet() {
  $q.bottomSheet({
    title: 'Choose an action',
    message: 'Select what you want to do',
    actions: [
      { label: 'Share', icon: 'share', id: 'share', color: 'primary' },
      { label: 'Copy', icon: 'content_copy', id: 'copy', color: 'secondary' },
      { label: 'Edit', icon: 'edit', id: 'edit', color: 'warning' },
      { label: 'Delete', icon: 'delete', id: 'delete', color: 'negative' },
    ],
  }).onOk((action) => {
    $q.notify({
      type: 'info',
      message: `Selected: ${action.label}`,
      position: 'top',
    })
  }).onCancel(() => {
    $q.notify({ type: 'info', message: 'Bottom sheet dismissed' })
  })
}
</script>
