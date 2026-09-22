<!--
LESSON 06 — Vue Router in Quasar
MEDIUM P02 — onBeforeRouteLeave Guard
============================================
CONCEPT: In-component guards hook navigation. onBeforeRouteLeave fires when
the user tries to leave — call next(false) to cancel, next() to allow. Ideal
for "unsaved changes" warnings.

PROBLEM: An edit form. A q-input bound to `formData` that sets
`hasUnsavedChanges` on edit, a Save button that clears the flag, and an
onBeforeRouteLeave guard using window.confirm — next(false) if the user
cancels.

TRY THIS: onBeforeRouteLeave((to, from, next) => {
  if (hasUnsavedChanges.value && !window.confirm('Leave?')) next(false); else next() })

EXPECTED OUTPUT: Typing then clicking "Go to About" pops a confirm; "Cancel"
keeps you on the page, "OK" navigates away.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
