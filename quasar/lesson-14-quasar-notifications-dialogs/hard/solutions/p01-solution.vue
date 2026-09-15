<template>
  <div class="q-pa-md">
    <q-btn label="Create Item" color="primary" @click="createItem" class="q-mr-sm" />
    <q-btn label="Update Item" color="warning" @click="updateItem" class="q-mr-sm" />
    <q-btn label="Delete Item" color="negative" @click="deleteItem" />
  </div>
</template>

<script setup>
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Composable: useCrudNotifications — wraps CRUD ops with consistent notifications
function useCrudNotifications() {
  function notifySuccess(message) {
    $q.notify({ type: 'positive', message, position: 'top', timeout: 3000 })
  }
  function notifyError(message) {
    $q.notify({ type: 'negative', message, position: 'top', timeout: 5000 })
  }
  function notifyLoading(message) {
    return $q.notify({ message, spinner: true, timeout: 0, position: 'center' })
  }
  function notifyDeleteWithUndo(itemName, onUndo) {
    $q.notify({
      type: 'negative',
      message: `Deleted: ${itemName}`,
      position: 'top',
      timeout: 5000,
      actions: [{ label: 'Undo', color: 'white', handler: onUndo }],
    })
  }

  return {
    create: async (itemName) => {
      const dismiss = notifyLoading('Creating...')
      try {
        await new Promise(r => setTimeout(r, 1000))
        dismiss()
        notifySuccess(`Created: ${itemName}`)
      } catch (e) {
        dismiss()
        notifyError(`Create failed: ${e.message}`)
      }
    },
    update: async (itemName) => {
      const dismiss = notifyLoading('Updating...')
      try {
        await new Promise(r => setTimeout(r, 1000))
        dismiss()
        notifySuccess(`Updated: ${itemName}`)
      } catch (e) {
        dismiss()
        notifyError(`Update failed: ${e.message}`)
      }
    },
    remove: async (itemName) => {
      const dismiss = notifyLoading('Deleting...')
      try {
        await new Promise(r => setTimeout(r, 800))
        dismiss()
        notifyDeleteWithUndo(itemName, () => {
          notifySuccess(`Undo: ${itemName} restored`)
        })
      } catch (e) {
        dismiss()
        notifyError(`Delete failed: ${e.message}`)
      }
    },
  }
}

const crud = useCrudNotifications()

function createItem() { crud.create('New Item') }
function updateItem() { crud.update('Existing Item') }
function deleteItem() { crud.remove('Target Item') }
</script>
