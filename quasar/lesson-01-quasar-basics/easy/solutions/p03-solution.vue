<!--
  Lesson 01 - Quasar Basics - Easy - Problem 03
  Toggle button showing/hiding a message using ref + v-if.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md">
    <!-- Clicking the button flips the boolean ref -->
    <q-btn
      :color="visible ? 'negative' : 'primary'"
      :label="visible ? 'Hide Message' : 'Show Message'"
      @click="visible = !visible"
    />

    <!-- v-if removes/adds the element from the DOM entirely -->
    <p v-if="visible" class="text-h6">Hello! You toggled me visible.</p>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// ref creates a reactive boolean; default hidden
const visible = ref(false)
</script>

<style scoped>
p {
  margin: 0;
}
</style>
