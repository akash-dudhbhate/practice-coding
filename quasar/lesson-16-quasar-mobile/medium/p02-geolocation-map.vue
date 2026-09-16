<!--
LESSON 16 — Quasar Mobile (Capacitor)
MEDIUM P02 — Geolocation + Map
============================================
CONCEPT: On Capacitor, Geolocation.checkPermissions()/requestPermissions()
precede getCurrentPosition(); on the web, navigator.geolocation wrapped in
a Promise does the same job. Map the result to an OpenStreetMap embed URL.

PROBLEM: A "Get My Location" button (loading state) filling a `location`
ref ({ latitude, longitude, accuracy }), a card displaying the coords, an
iframe map built from them, and typed error handling (permission-denied /
unavailable / unsupported) with notifications.

TRY THIS: const { Geolocation } = await import('@capacitor/geolocation');
const mapUrl = computed(() => `https://www.openstreetmap.org/export/embed.html?bbox=...&marker=${lat},${lng}`)

EXPECTED OUTPUT: Tapping the button fills in lat/long and renders a map;
denying permission shows a clear error toast.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
