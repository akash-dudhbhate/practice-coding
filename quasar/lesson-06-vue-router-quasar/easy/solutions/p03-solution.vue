<template>
  <!-- Page reading query params (?q=search&page=1) -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Search Results</div>
        <div class="text-subtitle1 q-mt-sm">Search term: {{ searchTerm }}</div>
        <div class="text-subtitle1">Page: {{ currentPage }}</div>
        <q-btn
          label="Next Page"
          color="primary"
          class="q-mt-md"
          @click="goToNextPage"
        />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

// Read query params from the route
const searchTerm = computed(() => route.query.q || '')
const currentPage = computed(() => Number(route.query.page) || 1)

// Navigate to the next page using router.push
function goToNextPage() {
  router.push({
    path: route.path,
    query: {
      q: route.query.q,
      page: currentPage.value + 1,
    },
  })
}
</script>

<style scoped>
.q-card {
  max-width: 400px;
  margin: 0 auto;
}
</style>
