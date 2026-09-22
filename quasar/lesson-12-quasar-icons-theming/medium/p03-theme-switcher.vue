<!--
PROBLEM: Theme Switcher (Medium)
=================================

CONCEPT: Runtime theming — overriding Quasar's --q-* CSS custom
properties and persisting the choice to localStorage.

TASK: Create a theme switcher: 3 theme buttons (blue, green, purple).
Clicking a button changes --q-primary and --q-secondary CSS variables
dynamically. Persist the selected theme to localStorage.

TRY THIS:
- Define a themes array with name/label/primary/secondary values
- applyTheme(): set the two CSS variables on document.documentElement
  via style.setProperty, then save the theme to localStorage
- Restore the saved theme when the component mounts
- Show a preview card so the change is visible

EXPECTED OUTPUT: Clicking a theme button instantly recolors the UI and
the choice survives a page reload.

CHECK: python3 check.py medium/p03

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: theme buttons + preview card -->
  </q-page>
</template>

<script setup>
// TODO: import ref + onMounted; themes array, applyTheme, restore saved
</script>
