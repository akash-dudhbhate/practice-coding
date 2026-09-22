<!--
LESSON 04 — Vue Composition API
MEDIUM P01 — Shopping Cart
============================================
CONCEPT: Combine ref() for the list, computed() for the derived total, and
plain functions for add/remove logic. .value.push() and .value.splice()
mutate a ref's array reactively.

PROBLEM: A shopping cart. `items` ref (array of { name, price }), inputs +
Add button to append items, a remove button per row, and a computed
`totalPrice` displayed at the bottom.

TRY THIS: const totalPrice = computed(() => items.value.reduce((s, i) => s + i.price, 0));
list rows with v-for="(item, index) in items"

EXPECTED OUTPUT: A form row (name + price + Add), a list of items each with
a remove button, and a "Total: $X" line that updates live.

CHECK: python3 check.py medium/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
