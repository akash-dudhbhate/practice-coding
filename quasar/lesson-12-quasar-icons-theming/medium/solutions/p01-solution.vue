<!--
  Lesson 12 - Medium - P01: Custom Brand Colors
  Demonstrates customizing brand colors in quasar.variables.scss and using
  color="primary" in buttons, cards, and icons.

  --- quasar.variables.scss (place in src/css/) ---
  // Override the primary brand color
  $primary   : #1976d2;  // Changed from default to custom blue
  $secondary : #26a69a;
  $accent    : #9c27b0;

  $dark      : #1d1d1d;
  $dark-page : #121212;

  $positive  : #21ba45;
  $negative  : #c10015;
  $info      : #31ccec;
  $warning   : #f2c037;
  ---
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Custom Brand Colors</div>

    <!-- Buttons using custom primary/secondary/accent colors -->
    <div class="q-mb-md q-gutter-md">
      <q-btn color="primary" label="Primary Button" no-caps />
      <q-btn color="secondary" label="Secondary Button" no-caps />
      <q-btn color="accent" label="Accent Button" no-caps />
    </div>

    <!-- Card using primary color -->
    <q-card class="my-card q-mb-md" flat bordered>
      <q-card-section class="bg-primary text-white">
        <div class="text-h6">Primary Card Header</div>
      </q-card-section>
      <q-card-section>
        <q-icon name="star" color="primary" size="32px" class="q-mr-sm" />
        <span class="text-body1">Icon with primary color inside card body</span>
      </q-card-section>
    </q-card>

    <!-- Icons using custom colors -->
    <div class="q-gutter-md">
      <q-icon name="favorite" color="primary" size="32px" />
      <q-icon name="bookmark" color="secondary" size="32px" />
      <q-icon name="lightbulb" color="accent" size="32px" />
    </div>

    <q-banner class="bg-blue-1 text-blue-8 q-mt-md">
      <template #avatar>
        <q-icon name="info" />
      </template>
      To customize colors, edit src/css/quasar.variables.scss and change
      $primary, $secondary, $accent values. See comments at top of this file.
    </q-banner>
  </q-page>
</template>

<script setup>
// The colors come from quasar.variables.scss overrides.
// After editing the .scss file, restart dev server for changes to take effect.
</script>

<style scoped>
.my-card {
  max-width: 400px;
}
</style>
