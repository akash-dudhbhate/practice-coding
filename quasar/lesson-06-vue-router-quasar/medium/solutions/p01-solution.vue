<template>
  <!-- Route configuration display (JS array in script) -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Route Configuration</div>
        <pre>{{ JSON.stringify(routes, null, 2) }}</pre>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
// Route configuration array with 3 routes: Home, About, 404 catch-all
// Lazy loading via dynamic import, meta titles for each route
const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('pages/HomePage.vue'),
    meta: { title: 'Home Page' },
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('pages/AboutPage.vue'),
    meta: { title: 'About Page' },
  },
  {
    path: '/:catchAll(.*)*',
    name: 'NotFound',
    component: () => import('pages/NotFoundPage.vue'),
    meta: { title: '404 Not Found' },
  },
]
</script>

<style scoped>
pre {
  white-space: pre-wrap;
  word-break: break-word;
}
</style>
