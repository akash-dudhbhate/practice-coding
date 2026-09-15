<template>
  <div class="q-pa-md">
    <q-btn label="Toggle Input" color="primary" @click="toggleInput" />
    <div v-if="showInput" class="q-mt-sm">
      <q-input ref="inputRef" v-model="text" label="Auto-focused input" />
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'

const showInput = ref(false)
const text = ref('')
const inputRef = ref(null)

async function toggleInput() {
  showInput.value = !showInput.value
  if (showInput.value) {
    // Wait for DOM to update, then focus the input
    await nextTick()
    inputRef.value?.focus()
  }
}
</script>
