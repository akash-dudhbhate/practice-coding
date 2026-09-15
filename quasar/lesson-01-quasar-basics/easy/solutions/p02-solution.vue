<!--
  Lesson 01 - Quasar Basics - Easy - Problem 02
  Two q-btn components with different colors.
-->
<template>
  <q-page class="flex flex-center q-gutter-md">
    <!-- "primary" is the default Quasar brand color -->
    <q-btn color="primary" label="Primary Button" />

    <!-- "negative" is typically red, used for destructive actions -->
    <q-btn color="negative" label="Negative Button" />
  </q-page>
</template>

<script setup>
// Static demo — no reactive state required.
</script>

<style scoped>
/* q-gutter-md on the flex container provides spacing between buttons */
</style>
