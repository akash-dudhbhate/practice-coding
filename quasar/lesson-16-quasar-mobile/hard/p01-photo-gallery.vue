<!--
LESSON 16 — Quasar Mobile (Capacitor)
HARD P01 — Mobile Photo Gallery
============================================
CONCEPT: Combine the pieces: Capacitor Camera for capture, a q-img grid for
thumbnails, a fullscreen q-dialog viewer with v-touch-swipe navigation,
v-touch-hold for delete, and Share for each photo. Always include the web
file-input fallback and an empty state.

PROBLEM: A gallery: Take Photo adds { id, dataUrl } to `photos` (Camera
plugin on capacitor, file input on web); grid of q-img thumbs; tap opens a
fullscreen viewer where swiping left/right navigates; long-press or a
delete button confirms via $q.dialog; per-photo share button. Empty state
when no photos.

TRY THIS: <q-img v-touch-hold="() => confirmDelete(photo.id)" .../>
<q-card-section v-touch-swipe.left="nextPhoto" v-touch-swipe.right="prevPhoto">

EXPECTED OUTPUT: Photos appear in a grid, tapping opens a swipeable viewer,
long-press deletes after confirm, share works per photo.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
