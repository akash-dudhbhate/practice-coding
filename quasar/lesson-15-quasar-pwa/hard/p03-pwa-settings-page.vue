<!--
LESSON 15 — Quasar PWA
HARD P03 — PWA Settings Page
============================================
CONCEPT: A settings hub gathers PWA state in one card: install status
(display-mode media query), service-worker update detection
(updatefound → SKIP_WAITING → reload), a push toggle that requests
permission, storage usage via navigator.storage.estimate(), and a cache
clear (caches.keys/delete) — all persisted.

PROBLEM: A settings card with: install-status row, update-available row
with Refresh button, push-notification q-toggle (requests permission),
storage usage text, and a "Clear Cache" button that confirms then deletes
all caches. Settings persist to localStorage.

TRY THIS: swRegistration.waiting.postMessage({ type: 'SKIP_WAITING' });
const { usage, quota } = await navigator.storage.estimate();
await Promise.all((await caches.keys()).map(k => caches.delete(k)))

EXPECTED OUTPUT: One card showing install/push/storage state with working
refresh, toggle, and cache-clear actions.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
