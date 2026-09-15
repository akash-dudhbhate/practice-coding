<template>
  <!-- Page that reads route param (:id) using useRoute() -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">User Detail</div>
        <div class="text-subtitle1 q-mt-md">User ID: {{ userId }}</div>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

// useRoute gives reactive access to the current route
const route = useRoute()

// Read the :id param from the route
const userId = computed(() => route.params.id)
</script>

<style scoped>
.q-card {
  max-width: 400px;
  margin: 0 auto;
}
</style>
