<!--
  Lesson 01 - Quasar Basics - Medium - Problem 03
  Add items to a list with q-input, q-btn, q-list.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md" style="max-width: 400px; margin: 0 auto;">
    <div class="row q-gutter-sm full-width">
      <!-- Bind input to newItem; press Enter or click Add to push -->
      <q-input
        v-model="newItem"
        label="Add an item"
        outlined
        class="col"
        @keyup.enter="addItem"
      />
      <q-btn color="primary" label="Add" @click="addItem" />
    </div>

    <!-- q-list renders the collection of items -->
    <q-list bordered separator class="full-width">
      <q-item v-for="(item, index) in items" :key="index">
        <q-item-section>{{ item }}</q-item-section>
        <q-item-section side>
          <q-btn flat dense color="negative" icon="delete" @click="removeItem(index)" />
        </q-item-section>
      </q-item>
    </q-list>

    <p v-if="items.length === 0" class="text-grey-7">No items yet. Add one above!</p>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Reactive list of items
const items = ref(['Learn Quasar', 'Build an app'])

// Temporary holder for the input field
const newItem = ref('')

// Add the typed item if non-empty, then clear the input
function addItem() {
  const trimmed = newItem.value.trim()
  if (trimmed) {
    items.value.push(trimmed)
    newItem.value = ''
  }
}

// Remove an item by index
function removeItem(index) {
  items.value.splice(index, 1)
}
</script>

<style scoped>
</style>
