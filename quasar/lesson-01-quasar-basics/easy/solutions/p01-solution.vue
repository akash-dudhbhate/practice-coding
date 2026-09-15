<!--
  Lesson 01 - Quasar Basics - Easy - Problem 01
  q-page wrapper with an h1 heading inside.
-->
<template>
  <!-- q-page is the standard content container inside a Quasar layout -->
  <q-page class="flex flex-center">
    <h1 class="text-h4 text-primary">Welcome to Quasar</h1>
  </q-page>
</template>

<script setup>
// No logic needed — this is a static page demonstrating q-page usage.
</script>

<style scoped>
/* Center the heading vertically and horizontally via flex utility classes */
h1 {
  margin: 0;
}
</style>
