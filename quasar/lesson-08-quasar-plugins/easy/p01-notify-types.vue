<!--
LESSON 08 — Quasar Plugins
EASY P01 — Four Notify Types
============================================
CONCEPT: $q.notify() fires toast notifications. The `type` option picks the
preset color/icon family: positive, negative, warning, info. Get $q from
useQuasar() inside <script setup>.

PROBLEM: Four q-btn buttons, each triggering $q.notify with a different
type — positive, negative, warning, info — each with its own message.

TRY THIS: const $q = useQuasar();
$q.notify({ type: 'positive', message: 'Operation successful!', timeout: 3000 })

EXPECTED OUTPUT: Four colored buttons; each pops a differently-styled toast.

CHECK: python3 check.py easy/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
