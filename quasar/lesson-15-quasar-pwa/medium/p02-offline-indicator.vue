<!--
LESSON 15 — Quasar PWA
MEDIUM P02 — Offline Indicator
============================================
CONCEPT: navigator.onLine reads connectivity now; 'online'/'offline' window
events fire on transitions. Register both in onMounted, remove both in
onUnmounted.

PROBLEM: An isOnline ref initialized from navigator.onLine; a negative
q-banner (wifi_off icon) shown only when offline; a positive $q.notify when
connectivity returns.

TRY THIS: const isOnline = ref(navigator.onLine);
window.addEventListener('online', onOnline); window.addEventListener('offline', onOffline)

EXPECTED OUTPUT: Cutting the network shows a red "You are offline" banner;
reconnecting hides it and toasts "Back online!".

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
