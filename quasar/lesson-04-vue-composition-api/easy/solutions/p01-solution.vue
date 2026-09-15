<!--
  Lesson 04 - Vue Composition API - Easy - Problem 01
  Counter using ref(0) with increment/decrement buttons.
  Uses <script setup>.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md">
    <div class="text-h2 text-primary">{{ count }}</div>

    <div class="row q-gutter-md">
      <q-btn color="negative" label="Decrement" @click="count--" />
      <q-btn color="primary" label="Increment" @click="count++" />
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// ref(0) creates a reactive number starting at 0
const count = ref(0)
</script>

<style scoped>
</style>
