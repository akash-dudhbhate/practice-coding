<!--
LESSON 16 — Quasar Mobile (Capacitor)
MEDIUM P03 — Share with Fallbacks
============================================
CONCEPT: Sharing degrades in three tiers: Capacitor Share plugin on mobile,
navigator.share (Web Share API) on modern browsers, then clipboard copy.
Treat user-cancel (AbortError) as a non-error.

PROBLEM: A card with share text + URL and a Share button trying all three
tiers in order, plus a separate "Copy Link" button on web using
navigator.clipboard (with a textarea/execCommand legacy fallback). Notify
on success and real failure.

TRY THIS: if ($q.platform.is.capacitor) { const { Share } = await import('@capacitor/share'); await Share.share({...}) }
else if (navigator.share) { await navigator.share({...}) } else { copyToClipboard() }

EXPECTED OUTPUT: Share opens the native sheet on mobile, the web share
sheet where supported, or copies to clipboard — each ending in a toast.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
