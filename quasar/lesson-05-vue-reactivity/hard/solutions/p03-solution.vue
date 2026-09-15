<template>
  <div class="q-pa-md">
    <p>First item name: {{ items[0]?.name }}</p>
    <q-btn label="Mutate nested (no UI update)" color="negative" @click="mutateNested" class="q-mr-sm" />
    <q-btn label="triggerRef (force update)" color="warning" @click="forceUpdate" class="q-mr-sm" />
    <q-btn label="Reassign .value (UI updates)" color="positive" @click="reassignValue" />
  </div>
</template>

<script setup>
import { shallowRef, triggerRef } from 'vue'

// shallowRef: only .value reassignment triggers reactivity
const items = shallowRef(
  Array.from({ length: 100 }, (_, i) => ({ id: i, name: `Item ${i}` }))
)

function mutateNested() {
  // This does NOT trigger a reactivity update (shallowRef)
  items.value[0].name = 'Mutated Name'
  console.log('Nested property changed (UI may not update):', items.value[0].name)
}

function forceUpdate() {
  // triggerRef forces a reactivity update after nested mutation
  triggerRef(items)
  console.log('triggerRef called — UI should now update')
}

function reassignValue() {
  // Reassigning .value DOES trigger reactivity
  items.value = [...items.value]
  items.value[0] = { ...items.value[0], name: 'Reassigned Name' }
  console.log('.value reassigned — UI updates')
}
</script>
