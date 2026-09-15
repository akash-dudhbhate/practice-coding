<!--
  Lesson 03 - Quasar Components - Easy - Problem 01
  q-card with image, title section, body text, two action buttons
  (Share, Read More).
-->
<template>
  <q-page class="flex flex-center">
    <q-card class="my-card" flat bordered>
      <!-- Card image -->
      <q-img src="https://cdn.quasar.dev/img/parallax2.jpg" ratio="16/9" />

      <!-- Title section -->
      <q-card-section>
        <div class="text-h6">Our Changing Planet</div>
        <div class="text-subtitle2">by John Doe</div>
      </q-card-section>

      <!-- Body text -->
      <q-card-section class="q-pt-none">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do
        eiusmod tempor incididunt ut labore et dolore magna aliqua.
      </q-card-section>

      <!-- Action buttons -->
      <q-card-actions align="around">
        <q-btn flat color="primary" label="Share" icon="share" />
        <q-btn flat color="primary" label="Read More" icon="article" />
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<script setup>
// Static card demo — no reactive state needed.
</script>

<style scoped>
.my-card {
  width: 100%;
  max-width: 350px;
}
</style>
