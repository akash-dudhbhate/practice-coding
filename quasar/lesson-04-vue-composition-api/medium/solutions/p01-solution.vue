<!--
  Lesson 04 - Vue Composition API - Medium - Problem 01
  Shopping cart: items ref (array of {name, price}),
  computed totalPrice, add/remove buttons. Display total.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md" style="max-width: 400px; margin: 0 auto;">
    <h2 class="text-h6">Shopping Cart</h2>

    <!-- Add new item -->
    <div class="row q-gutter-sm full-width">
      <q-input v-model="newItemName" label="Item name" outlined class="col" />
      <q-input v-model.number="newItemPrice" label="Price" outlined type="number" style="width: 100px;" />
      <q-btn color="primary" label="Add" @click="addItem" />
    </div>

    <!-- Cart items list -->
    <q-list bordered separator class="full-width">
      <q-item v-for="(item, index) in items" :key="index">
        <q-item-section>
          <q-item-label>{{ item.name }}</q-item-label>
          <q-item-label caption>${{ item.price.toFixed(2) }}</q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-btn flat dense color="negative" icon="remove_circle" @click="removeItem(index)" />
        </q-item-section>
      </q-item>
    </q-list>

    <!-- Total price (computed) -->
    <div class="full-width text-right">
      <span class="text-h6">Total: </span>
      <span class="text-h6 text-primary">${{ totalPrice.toFixed(2) }}</span>
    </div>
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue'

// Cart items: array of objects with name and price
const items = ref([
  { name: 'Coffee Mug', price: 12.99 },
  { name: 'Notebook', price: 5.49 },
])

// Temporary holders for the add-item form
const newItemName = ref('')
const newItemPrice = ref(0)

// Computed total: recalculates only when items changes
const totalPrice = computed(() =>
  items.value.reduce((sum, item) => sum + item.price, 0)
)

// Add a new item to the cart
function addItem() {
  if (newItemName.value.trim() && newItemPrice.value > 0) {
    items.value.push({ name: newItemName.value.trim(), price: newItemPrice.value })
    newItemName.value = ''
    newItemPrice.value = 0
  }
}

// Remove an item by index
function removeItem(index) {
  items.value.splice(index, 1)
}
</script>

<style scoped>
</style>
