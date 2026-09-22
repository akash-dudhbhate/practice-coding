<!--
LESSON 16 — Quasar Mobile (Capacitor)
HARD P02 — Mobile-Aware App Shell
============================================
CONCEPT: A production shell detects web/iOS/Android via $q.platform, swaps
drawer↔bottom-tabs, fires haptics (Capacitor Haptics.impact) on taps when
native, and respects env(safe-area-inset-*) so notches don't cover UI.

PROBLEM: A q-layout shell: platform label/icon/class in the toolbar, drawer
nav on desktop + bottom q-tabs on mobile (3 shared items), a hapticTap(fn)
helper that runs the callback then vibrates on capacitor, and CSS using
env(safe-area-inset-top/bottom/left/right) plus per-platform classes.

TRY THIS: async function hapticTap(cb) { cb(); if (!$q.platform.is.capacitor) return;
  const { Haptics, ImpactStyle } = await import('@capacitor/haptics');
  await Haptics.impact({ style: ImpactStyle.Light }) }
.safe-area-bottom { padding-bottom: env(safe-area-inset-bottom) }

EXPECTED OUTPUT: Correct chrome per platform with haptic taps on device
and content clear of notches.

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
