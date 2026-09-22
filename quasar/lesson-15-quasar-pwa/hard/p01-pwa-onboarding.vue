<!--
LESSON 15 — Quasar PWA
HARD P01 — PWA Onboarding Card
============================================
CONCEPT: Onboarding = standalone check + beforeinstallprompt capture + a
benefits pitch + polite dismissal. Persist "dismissed" to localStorage so
you don't nag on every visit.

PROBLEM: A card shown only when the app is NOT installed and the user
hasn't dismissed it — listing PWA benefits (offline, installable, push)
with icons, an Install button wired to the deferred prompt, and a "Maybe
later" button persisting dismissal. An "installed" banner otherwise.

TRY THIS: showOnboarding = !isStandalone && localStorage.getItem('pwa_onboarding_dismissed') !== 'true';
dismiss() sets the flag and hides the card.

EXPECTED OUTPUT: Browser users get a benefits card with Install / Maybe
later; installed users see a confirmation banner; dismissal sticks.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
