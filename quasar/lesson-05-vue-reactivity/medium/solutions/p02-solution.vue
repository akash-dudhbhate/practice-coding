<template>
  <div class="q-pa-md">
    <p>Count: {{ state.count }}</p>
    <p>Name: {{ state.name }}</p>
    <q-btn label="Increment" color="primary" @click="state.count++" />
    <q-btn label="Change Name" color="secondary" @click="state.name = 'Bob'" class="q-ml-sm" />
  </div>
</template>

<script setup>
import { reactive, watch } from 'vue'

const state = reactive({ count: 0, name: 'Alice' })

// Watch specific property using getter function
watch(
  () => state.count,
  (newVal, oldVal) => {
    console.log(`count changed: ${oldVal} → ${newVal}`)
  }
)

// Watch multiple sources
watch(
  [() => state.count, () => state.name],
  ([newCount, newName], [oldCount, oldName]) => {
    console.log(`count: ${oldCount}→${newCount}, name: ${oldName}→${newName}`)
  }
)
</script>
