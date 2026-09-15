<!--
  Lesson 01 - Quasar Basics - Medium - Problem 02
  Counter with increment/decrement/reset buttons.
  Decrement is disabled when count is 0.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md">
    <div class="text-h2 text-primary">{{ count }}</div>

    <div class="row q-gutter-md">
      <!-- Decrement disabled at 0 to prevent negative counts -->
      <q-btn
        color="negative"
        label="Decrement"
        :disable="count === 0"
        @click="count--"
      />
      <q-btn color="primary" label="Increment" @click="count++" />
      <q-btn color="grey-7" label="Reset" outline @click="count = 0" />
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Counter starts at zero
const count = ref(0)
</script>

<style scoped>
</style>
