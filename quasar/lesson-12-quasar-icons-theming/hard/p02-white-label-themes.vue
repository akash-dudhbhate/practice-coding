<!--
PROBLEM: White-Label Theme System (Hard)
=========================================

CONCEPT: Runtime color customization — q-color picker in a popup proxy,
live CSS variable updates, localStorage persistence, reset to defaults.

TASK: Build a white-label theme system: a settings page where users can
customize primary, secondary, and accent colors with color pickers.
Changes apply live and persist to localStorage. Include a "reset to
default" button.

TRY THIS:
- Keep a reactive theme object { primary, secondary, accent }
- Each color: an input with an icon + popup proxy containing a color picker
- On change: set the matching --q-* CSS variables and save to localStorage
- Restore saved values on mount; reset restores a default theme object
- Add a live preview section so changes are visible

EXPECTED OUTPUT: Picking a color instantly re-themes the preview (and the
app). Reload keeps your choices; Reset returns to the default palette.

CHECK: python3 check.py hard/p02

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: 3 color-picker inputs + reset button + live preview -->
  </q-page>
</template>

<script setup>
// TODO: reactive theme, applyTheme (CSS vars + localStorage), resetTheme
</script>
