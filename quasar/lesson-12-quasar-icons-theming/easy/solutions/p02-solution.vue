<!--
  Lesson 12 - Easy - P02: Typography & Spacing Utilities
  Demonstrates Quasar typography classes (text-h4, text-subtitle1, text-body1,
  text-caption) and spacing utilities (q-pa-md, q-mt-lg).
-->
<template>
  <q-page class="q-pa-md">
    <!-- q-pa-md adds padding; q-mt-lg adds top margin -->
    <div class="q-pa-md q-mt-lg">
      <!-- Typography hierarchy -->
      <div class="text-h4">Main Title (text-h4)</div>
      <div class="text-subtitle1 q-mt-sm">Subtitle goes here (text-subtitle1)</div>
      <p class="text-body1 q-mt-md">
        This is the body paragraph using text-body1. It provides comfortable
        reading size for main content. Quasar typography classes follow
        Material Design guidelines for font sizes and weights.
      </p>
      <div class="text-caption q-mt-sm">
        Note: This is a small caption using text-caption for secondary info.
      </div>
    </div>

    <!-- Another section demonstrating spacing -->
    <q-separator class="q-mt-lg q-mb-lg" />

    <div class="q-pa-md">
      <div class="text-h5">Spacing Utilities</div>
      <p class="text-body2 q-mt-md">
        q-pa-md = padding on all sides (medium).
        q-mt-lg = margin top (large).
        These utility classes follow a pattern: q-[property][side]-[size].
      </p>
    </div>
  </q-page>
</template>

<script setup>
// No script logic needed — this is a pure CSS/utility demonstration.
</script>

<style scoped>
</style>
