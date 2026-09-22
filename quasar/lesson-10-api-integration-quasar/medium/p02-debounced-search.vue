<!--
LESSON 10 — API Integration in Quasar
MEDIUM P02 — Debounced Search + AbortController
============================================
CONCEPT: q-input's `debounce` attr delays v-model updates; AbortController
lets you cancel the previous in-flight fetch so stale results never
overwrite fresh ones (check e.name !== 'AbortError' in catch).

PROBLEM: A search box (debounce ~400) that queries a users API with
?name_like=, aborts the previous request on each new keystroke, shows
loading/error/empty states, and lists name + email results.

TRY THIS: if (currentController) currentController.abort();
currentController = new AbortController();
fetch(url, { signal: currentController.signal })

EXPECTED OUTPUT: Typing filters users after a pause; rapid typing cancels
stale requests; "No results found" shows on empty.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
