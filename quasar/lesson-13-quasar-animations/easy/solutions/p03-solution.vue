<!--
  Lesson 13 - Easy - P03: Skeleton Loading
  Shows skeleton placeholders for 2 seconds (setTimeout), then displays
  actual content (image, title, text). Skeleton sizes match content.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Skeleton Loading</div>

    <q-card flat bordered style="max-width: 400px">
      <!-- Skeleton state: shown while loading -->
      <template v-if="loading">
        <q-skeleton height="200px" square animation="wave" />
        <q-card-section>
          <q-skeleton type="text" width="60%" height="24px" class="q-mb-sm" animation="wave" />
          <q-skeleton type="text" width="90%" animation="wave" />
          <q-skeleton type="text" width="85%" animation="wave" />
          <q-skeleton type="text" width="70%" animation="wave" />
        </q-card-section>
      </template>

      <!-- Actual content: shown after loading completes -->
      <template v-else>
        <q-img src="https://cdn.quasar.dev/img/parallax2.jpg" height="200px" />
        <q-card-section>
          <div class="text-h6">Beautiful Landscape</div>
          <p class="text-body2 text-grey-8">
            This is the actual content that replaces the skeleton loaders.
            The skeleton sizes were designed to match this content for a
            seamless transition.
          </p>
        </q-card-section>
      </template>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const loading = ref(true)

// Simulate content loading with a 2-second delay
onMounted(() => {
  setTimeout(() => {
    loading.value = false
  }, 2000)
})
</script>

<style scoped>
</style>
