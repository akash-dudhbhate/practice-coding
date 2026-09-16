<!--
LESSON 08 — Quasar Plugins
MEDIUM P03 — Loading Spinner on Submit
============================================
CONCEPT: $q.loading.show() blocks the UI with a spinner overlay; always pair
it with $q.loading.hide() in a finally block so the overlay clears even on
error.

PROBLEM: A q-form (name + email q-inputs with rules) whose submit handler
shows $q.loading, awaits a simulated 2-second save (setTimeout Promise),
then fires a positive $q.notify — hiding the spinner in finally.

TRY THIS: $q.loading.show({ message: 'Saving...' });
await new Promise(r => setTimeout(r, 2000));
... finally { $q.loading.hide() }

EXPECTED OUTPUT: Submitting shows a full-screen "Saving your data..."
spinner for ~2s, then a success toast.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
