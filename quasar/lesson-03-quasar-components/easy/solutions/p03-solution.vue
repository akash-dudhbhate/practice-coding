<!--
  Lesson 03 - Quasar Components - Easy - Problem 03
  q-tabs with 3 tabs (Overview, Details, Reviews) and matching
  q-tab-panels with text content.
-->
<template>
  <q-page class="flex flex-center column" style="max-width: 500px; margin: 0 auto;">
    <!-- Tab bar -->
    <q-tabs
      v-model="activeTab"
      class="text-primary full-width"
      indicator-color="primary"
      align="justify"
    >
      <q-tab name="overview" label="Overview" />
      <q-tab name="details" label="Details" />
      <q-tab name="reviews" label="Reviews" />
    </q-tabs>

    <!-- Tab panels: each q-tab-panel matches a q-tab by name -->
    <q-tab-panels v-model="activeTab" animated class="full-width">
      <q-tab-panel name="overview">
        <div class="text-h6">Overview</div>
        <p>This is the overview tab. It provides a high-level summary of the product.</p>
      </q-tab-panel>

      <q-tab-panel name="details">
        <div class="text-h6">Details</div>
        <p>This is the details tab. Here you'll find specifications and technical information.</p>
      </q-tab-panel>

      <q-tab-panel name="reviews">
        <div class="text-h6">Reviews</div>
        <p>This is the reviews tab. Read what other users have to say about this product.</p>
      </q-tab-panel>
    </q-tab-panels>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Currently active tab name
const activeTab = ref('overview')
</script>

<style scoped>
</style>
