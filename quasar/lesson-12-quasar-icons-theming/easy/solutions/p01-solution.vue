<!--
  Lesson 12 - Easy - P01: Basic Icons
  5 different icons (home, settings, user, bell, search) with different
  sizes and colors, displayed in a row with labels.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Quasar Icons Showcase</div>

    <div class="row items-center q-gutter-xl">
      <!-- Each icon has a different size and color -->
      <div class="column items-center q-gutter-sm">
        <q-icon name="home" size="32px" color="primary" />
        <span>Home</span>
      </div>

      <div class="column items-center q-gutter-sm">
        <q-icon name="settings" size="40px" color="secondary" />
        <span>Settings</span>
      </div>

      <div class="column items-center q-gutter-sm">
        <q-icon name="person" size="28px" color="accent" />
        <span>User</span>
      </div>

      <div class="column items-center q-gutter-sm">
        <q-icon name="notifications" size="36px" color="warning" />
        <span>Bell</span>
      </div>

      <div class="column items-center q-gutter-sm">
        <q-icon name="search" size="24px" color="info" />
        <span>Search</span>
      </div>
    </div>
  </q-page>
</template>

<script setup>
// Icons are rendered using Material Icons (default icon set in Quasar).
// size prop accepts px values; color prop uses Quasar color palette.
</script>

<style scoped>
</style>
