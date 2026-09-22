<!--
LESSON 06 — Vue Router in Quasar
EASY P01 — Read a Route Param
============================================
CONCEPT: Routes like /users/:id put dynamic values in route.params. Inside
<script setup> you grab the current route with useRoute() and read params
reactively — wrap it in a computed so it updates on navigation.

PROBLEM: A user detail page. useRoute() to get the route, a computed
`userId` reading route.params.id, displayed as "User ID: X" in a q-card.

TRY THIS: const route = useRoute();
const userId = computed(() => route.params.id)

EXPECTED OUTPUT: A card titled "User Detail" showing the id from the URL,
e.g. "User ID: 42" on /users/42.

CHECK: python3 check.py easy/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
