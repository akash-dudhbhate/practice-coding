<!--
LESSON 06 — Vue Router in Quasar
HARD P02 — beforeEach Auth Guard
============================================
CONCEPT: A global beforeEach guard inspects every navigation. Check the
token in localStorage, then use route meta flags: requiresAuth without a
token redirects to /login (carrying redirect: to.fullPath), guestOnly with a
token redirects to /dashboard.

PROBLEM: An exported `beforeEachGuard(to, from, next)` function doing
exactly that: localStorage.getItem('token'), requiresAuth → /login with
redirect query, guestOnly → /dashboard, else next().

TRY THIS: if (to.meta.requiresAuth && !isAuthenticated) next({ path: '/login', query: { redirect: to.fullPath } })

EXPECTED OUTPUT: The guard function in the script (optionally shown in a
<pre>), ready to be wired with router.beforeEach(guard).

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
