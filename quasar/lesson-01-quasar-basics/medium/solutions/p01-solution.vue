<!--
  Lesson 01 - Quasar Basics - Medium - Problem 01
  q-input with v-model, real-time display of typed text below.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md">
    <!-- v-model two-way binds the input value to the `text` ref -->
    <q-input
      v-model="text"
      label="Type something..."
      outlined
      style="min-width: 300px"
    />

    <!-- Display updates instantly because `text` is reactive -->
    <div>
      <span class="text-grey-7">You typed: </span>
      <span class="text-primary text-weight-bold">{{ text }}</span>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Holds the current input value; empty string by default
const text = ref('')
</script>

<style scoped>
</style>
