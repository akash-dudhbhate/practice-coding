<!--
LESSON 06 — Vue Router in Quasar
MEDIUM P01 — Route Config Array
============================================
CONCEPT: A routes array maps paths to components. Lazy-load pages with
() => import('pages/X.vue') so each route is code-split, and attach
meta: { title } for document titles or guard checks.

PROBLEM: A `routes` array in the script with 3 routes — Home (/), About
(/about), and a 404 catch-all '/:catchAll(.*)*' — all lazy-loaded, all with
meta titles. Display the config in a <pre>.

TRY THIS: { path: '/', name: 'Home', component: () => import('pages/HomePage.vue'), meta: { title: 'Home Page' } }

EXPECTED OUTPUT: A card rendering the routes array as JSON showing all three
routes with their lazy imports and meta titles.

CHECK: python3 check.py medium/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
