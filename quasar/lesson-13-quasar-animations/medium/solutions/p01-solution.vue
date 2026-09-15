<!--
  Lesson 13 - Medium - P01: Animated List with TransitionGroup
  Add button adds a random item. Remove button per item.
  Items animate in (slide from left) and out (slide to right).
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Animated List</div>

    <q-btn color="primary" icon="add" label="Add Item" no-caps class="q-mb-md" @click="addItem" />

    <!-- TransitionGroup animates each list item enter/leave -->
    <TransitionGroup tag="div" name="list" class="q-gutter-sm">
      <div v-for="item in items" :key="item.id" class="list-item row items-center justify-between">
        <span>{{ item.text }}</span>
        <q-btn flat dense round icon="close" color="negative" @click="removeItem(item.id)" />
      </div>
    </TransitionGroup>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

let nextId = 1
const words = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew']

const items = ref([
  { id: nextId++, text: 'Apple' },
  { id: nextId++, text: 'Banana' },
])

// Add a random item to the list
function addItem() {
  const word = words[Math.floor(Math.random() * words.length)]
  items.value.push({ id: nextId++, text: `${word} #${nextId - 1}` })
}

// Remove item by id
function removeItem(id) {
  items.value = items.value.filter((item) => item.id !== id)
}
</script>

<style scoped>
.list-item {
  padding: 12px 16px;
  background: #e8eaf6;
  border-radius: 8px;
  transition: all 0.4s ease;
}

/* Enter: slide in from the left */
.list-enter-from {
  opacity: 0;
  transform: translateX(-30px);
}
.list-enter-to {
  opacity: 1;
  transform: translateX(0);
}

/* Leave: slide out to the right */
.list-leave-from {
  opacity: 1;
  transform: translateX(0);
}
.list-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

/* Leave-active: position absolute so removing items don't block layout */
.list-leave-active {
  position: absolute;
}

/* Move transition for items that shift position */
.list-move {
  transition: transform 0.4s ease;
}
</style>
