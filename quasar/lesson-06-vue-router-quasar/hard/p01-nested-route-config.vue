<!--
LESSON 06 — Vue Router in Quasar
HARD P01 — Nested Route Configuration
============================================
CONCEPT: Layout routes wrap child routes — the layout renders chrome
(header/drawer) and a <router-view> where the child page appears. Two
layouts (MainLayout, BlankLayout) let you give auth pages a different shell.

PROBLEM: A `routes` array with two top-level layout routes. MainLayout has
children Home, Dashboard, Settings; BlankLayout has children Login,
Register. Dashboard and Settings carry meta: { requiresAuth: true }, auth
pages meta: { guestOnly: true }. Display the config in a <pre>.

TRY THIS: { path: '/', component: () => import('layouts/MainLayout.vue'),
  children: [ { path: 'dashboard', ..., meta: { requiresAuth: true } } ] }

EXPECTED OUTPUT: The full nested config rendered as JSON — both layouts,
five pages, correct meta flags.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
