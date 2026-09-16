<!--
LESSON 18 — Quasar SSR
MEDIUM P01 — preFetch Product Page
============================================
CONCEPT: A `preFetch({ store, currentRoute })` export runs on the server
before render (and again on client nav). Store results in Pinia / initial
state so the server HTML already contains the data.

PROBLEM: A product page: export a preFetch that reads
currentRoute.params.id, fetches the product (a simulated Promise is fine),
stores it, and handles not-found errors; the template renders
name/description/price with loading and error states.

TRY THIS: export async function preFetch({ store, currentRoute }) {
  const product = await fetchProduct(currentRoute.params.id); store.product = product }
(Note: in <script setup>, define then `export { preFetch }`.)

EXPECTED OUTPUT: View-source on /product/42 shows the product name in the
initial HTML.

CHECK: python3 check.py medium/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
