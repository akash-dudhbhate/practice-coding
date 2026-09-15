<!--
  File Editor Component (Electron renderer)
  -----------------------------------------
  Uses the safe API exposed by the preload script (window.electronAPI)
  to open a file via the native dialog, display its content in a text
  area, and save it back to disk.

  - "Open" button calls electronAPI.readFile()
  - Content is shown in a QInput type="textarea"
  - "Save" button calls electronAPI.saveFile(fileName, content)
  - Handles cancel (null return) and errors gracefully
-->
<template>
  <q-page class="q-pa-md">
    <div class="row items-center justify-between q-mb-md">
      <div class="text-h6">
        {{ fileName || 'Untitled' }}
        <q-badge v-if="dirty" color="orange" label="unsaved" class="q-ml-sm" />
      </div>
      <div class="row q-gutter-sm">
        <q-btn color="primary" icon="folder_open" label="Open" @click="openFile" />
        <q-btn
          color="positive"
          icon="save"
          label="Save"
          :disable="!content"
          @click="saveFile"
        />
      </div>
    </div>

    <!-- Editor area -->
    <q-input
      v-model="content"
      type="textarea"
      filled
      autogrow
      input-style="font-family: monospace; font-size: 14px; min-height: 400px"
      placeholder="Open a file or start typing…"
      @update:model-value="onContentChange"
    />
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const fileName = ref('')
const content = ref('')
const dirty = ref(false)

/**
 * Open a file via the Electron main process dialog.
 */
async function openFile() {
  try {
    const result = await window.electronAPI.readFile()

    // User cancelled the dialog
    if (result === null) {
      return
    }

    // Error returned from the main process
    if (result.error) {
      $q.notify({ type: 'negative', message: `Open failed: ${result.error}` })
      return
    }

    fileName.value = result.name
    content.value = result.content
    dirty.value = false
    $q.notify({ type: 'positive', message: `Opened ${result.name}` })
  } catch (err) {
    $q.notify({ type: 'negative', message: `Error: ${err.message}` })
  }
}

/**
 * Save the current content to disk.
 */
async function saveFile() {
  try {
    const saved = await window.electronAPI.saveFile(fileName.value, content.value)

    if (saved) {
      dirty.value = false
      $q.notify({ type: 'positive', message: 'File saved' })
    } else {
      // User cancelled the save dialog
      $q.notify({ type: 'info', message: 'Save cancelled' })
    }
  } catch (err) {
    $q.notify({ type: 'negative', message: `Save failed: ${err.message}` })
  }
}

/**
 * Mark the document as dirty whenever the text changes.
 */
function onContentChange() {
  dirty.value = true
}
</script>

<style scoped>
.q-page {
  max-width: 900px;
  margin: 0 auto;
}
</style>
