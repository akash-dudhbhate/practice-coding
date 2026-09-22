<!--
LESSON 16 — Quasar Mobile (Capacitor)
HARD P03 — Offline-First Mobile App
============================================
CONCEPT: Offline-first = cache reads/writes through a storage abstraction
(Capacitor Storage on mobile, localStorage on web), flag items synced vs
pending, resync on the 'online' event, and give the user v-touch-pull
pull-to-refresh plus haptic feedback.

PROBLEM: An items list app: initStorage() choosing the backend by platform,
loadCached/persistCache around 'cached_items', online/offline banner +
listeners, syncPending on reconnect, add-item input working offline
(synced flag), pull-to-refresh (v-touch-pull threshold ~80) re-fetching,
and a haptic() helper.

TRY THIS: v-touch-pull="onPull" where onPull fires fetchItems() when
pullAmount > 80; storageGet/storageSet wrap Storage.get/set or localStorage.

EXPECTED OUTPUT: Items persist across reload, offline adds show "pending"
badges, reconnecting syncs them, pulling down refreshes with haptics.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
