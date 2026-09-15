<!--
  Lesson 04 - Vue Composition API - Hard - Problem 01
  Composable useCounter inline returning {count, double, increment,
  decrement, reset}. Use in component. Display count and double.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md">
    <h2 class="text-h6">useCounter Composable</h2>

    <!-- Display count and its doubled value -->
    <div class="text-h4 text-primary">{{ count }}</div>
    <div class="text-subtitle1 text-grey-7">Doubled: {{ double }}</div>

    <!-- Action buttons -->
    <div class="row q-gutter-md">
      <q-btn color="negative" label="Decrement" @click="decrement" />
      <q-btn color="grey-7" label="Reset" outline @click="reset" />
      <q-btn color="primary" label="Increment" @click="increment" />
    </div>
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue'

/**
 * Inline composable: useCounter
 * Encapsulates counter logic with count, a doubled computed value,
 * and increment/decrement/reset functions.
 * In a real app, this would live in src/composables/useCounter.js
 * and be imported with `import { useCounter } from 'composables/useCounter'`.
 */
function useCounter() {
  const count = ref(0)
  const double = computed(() => count.value * 2)

  function increment() {
    count.value++
  }

  function decrement() {
    count.value--
  }

  function reset() {
    count.value = 0
  }

  return { count, double, increment, decrement, reset }
}

// Destructure the composable's return value for use in the template
const { count, double, increment, decrement, reset } = useCounter()
</script>

<style scoped>
</style>
