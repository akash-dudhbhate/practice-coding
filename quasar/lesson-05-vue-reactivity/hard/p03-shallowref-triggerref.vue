<!--
LESSON 05 — Vue Reactivity System
HARD P03 — shallowRef + triggerRef
============================================
CONCEPT: shallowRef() only tracks .value reassignment — mutating a nested
property is invisible to Vue. triggerRef() forces an update anyway. Use it
for large data where deep tracking costs too much.

PROBLEM: A `items` shallowRef holding 100 generated objects ({ id, name }).
Three buttons: one mutates items.value[0].name (no UI update), one calls
triggerRef(items) to force the update, one reassigns items.value (UI updates
on its own). Display items[0]?.name.

TRY THIS: items.value[0].name = 'Mutated Name' → nothing; triggerRef(items) →
updates; items.value = [...items.value] → updates

EXPECTED OUTPUT: The first item's name shown; button 1 appears to do
nothing, button 2 reveals the mutation, button 3 changes it directly.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
