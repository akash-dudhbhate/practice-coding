<!--
LESSON 15 — Quasar PWA
EASY P03 — Custom Install Button
============================================
CONCEPT: The browser fires 'beforeinstallprompt' when the app is
installable — preventDefault() it and stash the event. Later call
prompt() on it and await userChoice ('accepted'/'dismissed'), then drop
the reference — it can only be used once.

PROBLEM: An "Install App" q-btn that only appears once
beforeinstallprompt fires (canInstall ref). Clicking calls
deferredPrompt.prompt(), reads userChoice, hides the button afterwards,
and notifies accepted/declined. Also listen for 'appinstalled'.

TRY THIS: window.addEventListener('beforeinstallprompt', e => {
  e.preventDefault(); deferredPrompt = e; canInstall.value = true })
const { outcome } = await deferredPrompt.userChoice

EXPECTED OUTPUT: The button appears when installable, triggers the native
prompt, and disappears — a banner confirms a successful install.

CHECK: python3 check.py easy/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
