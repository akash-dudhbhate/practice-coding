<template>
  <div class="q-pa-md">
    <h6>Rich Text Editor with Live Preview</h6>
    <q-editor
      v-model="content"
      :toolbar="[
        ['bold', 'italic', 'underline', 'strike'],
        ['unordered', 'ordered'],
        ['link', 'quote', 'code'],
        ['undo', 'redo']
      ]"
      min-height="150px"
    />

    <q-separator class="q-my-md" />

    <h6>Live Preview</h6>
    <q-card flat bordered>
      <q-card-section>
        <div v-html="sanitizedContent"></div>
      </q-card-section>
    </q-card>

    <div class="q-mt-md">
      <q-btn label="Save" color="primary" @click="save" class="q-mr-sm" />
      <q-btn label="Clear" color="negative" @click="clear" />
    </div>

    <q-banner v-if="savedContent" class="bg-positive text-white q-mt-md">
      Saved content: {{ savedContent.substring(0, 50) }}...
    </q-banner>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()
const content = ref('<p>Start typing here...</p>')
const savedContent = ref('')

// Basic HTML sanitization: remove script tags and event handlers
const sanitizedContent = computed(() => {
  let html = content.value
  // Remove <script> tags
  html = html.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
  // Remove on* event handlers
  html = html.replace(/\son\w+="[^"]*"/gi, '')
  html = html.replace(/\son\w+='[^']*'/gi, '')
  return html
})

function save() {
  savedContent.value = sanitizedContent.value
  $q.notify({ type: 'positive', message: 'Content saved!' })
}

function clear() {
  content.value = ''
  savedContent.value = ''
  $q.notify({ type: 'info', message: 'Editor cleared' })
}
</script>
