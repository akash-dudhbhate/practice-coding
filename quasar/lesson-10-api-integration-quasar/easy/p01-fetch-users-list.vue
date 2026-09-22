<!--
LESSON 10 — API Integration in Quasar
EASY P01 — Fetch Users with Loading/Error States
============================================
CONCEPT: fetch() returns a Response — check res.ok before res.json(). Keep
three refs (data, loading, error) and render a different element for each
state; kick the request off in onMounted.

PROBLEM: A component that fetches users from a public API
(jsonplaceholder.typicode.com/users). Show a spinner/progress while
loading, a banner on error, and a q-list of name + email on success.

TRY THIS: const res = await fetch(API); if (!res.ok) throw new Error(`HTTP ${res.status}`);
users.value = await res.json(); onMounted(fetchUsers)

EXPECTED OUTPUT: Progress bar → then a list of user names and emails; a bad
URL shows the error banner instead.

CHECK: python3 check.py easy/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
