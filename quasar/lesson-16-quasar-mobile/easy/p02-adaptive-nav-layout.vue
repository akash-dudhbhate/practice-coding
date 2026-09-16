<!--
LESSON 16 — Quasar Mobile (Capacitor)
EASY P02 — Adaptive Navigation Layout
============================================
CONCEPT: $q.platform.is.mobile / .is.desktop lets one codebase serve both
form factors — a left q-drawer on desktop, bottom q-tabs in a q-footer on
mobile. Both share one activeTab ref.

PROBLEM: A q-layout with: header toolbar (menu button + drawer only on
desktop, `show-if-above`), a q-list nav drawer with 3 items, a q-footer with
q-tabs shown only on mobile — same 3 items (home/search/profile) in both.

TRY THIS: v-if="$q.platform.is.desktop" on the drawer;
v-if="$q.platform.is.mobile" on the footer; v-model="activeTab" on both.

EXPECTED OUTPUT: Desktop shows a hamburger + left drawer; phones show a
bottom tab bar; both highlight the same active tab.

CHECK: python3 check.py easy/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
