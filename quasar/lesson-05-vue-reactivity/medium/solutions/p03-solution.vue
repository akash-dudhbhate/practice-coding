<template>
  <div class="q-pa-md">
    <q-input v-model="name" label="Name" />
    <q-input v-model="email" label="Email" />
    <p>Name: {{ name }}</p>
    <p>Email: {{ email }}</p>
  </div>
</template>

<script setup>
import { reactive, toRefs, watch } from 'vue'

const form = reactive({ name: 'Alice', email: 'alice@test.com' })

// toRefs preserves reactivity when destructuring
const { name, email } = toRefs(form)

// Watch one destructured ref — reactivity is preserved
watch(name, (newVal, oldVal) => {
  console.log(`name changed: ${oldVal} → ${newVal}`)
})
</script>
