<!--
PROBLEM: Custom Dark Mode Styles (Medium)
==========================================

CONCEPT: Quasar dark mode — $q.dark.set()/toggle(), and the .body--dark
CSS class Quasar applies to <body> for custom dark styling.

TASK: Create a component with custom dark mode styles. Use .body--dark
to change a card's background and text color. Toggle dark mode and
verify the styles adapt.

TRY THIS:
- A toggle bound to dark mode that calls the Quasar dark setter
- One or two cards with a custom class
- Scoped CSS: light styles on the class; dark overrides under
  body--dark (use :global() or a global stylesheet to reach <body>)
- Add a transition so the change is smooth

EXPECTED OUTPUT: Flipping the toggle switches Quasar dark mode and the
cards swap background/text colors via your custom CSS.

CHECK: python3 check.py medium/p02

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: dark-mode toggle + styled cards -->
  </q-page>
</template>

<script setup>
// TODO: import ref + useQuasar; wire a toggle to Quasar dark mode
</script>

<style scoped>
/* TODO: light styles on your card class + body--dark overrides */
</style>
