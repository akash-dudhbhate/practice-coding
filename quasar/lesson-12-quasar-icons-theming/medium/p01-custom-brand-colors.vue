<!--
PROBLEM: Custom Brand Colors (Medium)
======================================

CONCEPT: Theming via quasar.variables.scss — overriding $primary,
$secondary, $accent and using them through color props and bg- classes.

TASK: Customize brand colors in quasar.variables.scss (change primary to
a custom color). Create a component that uses color="primary" in buttons,
cards, and icons. Verify the custom color applies.

TRY THIS:
- Put the SCSS override block in a comment at the top of this file
  (it belongs in src/css/quasar.variables.scss in a real app)
- Buttons: color="primary" / "secondary" / "accent"
- Card header: bg-primary text-white
- Icons: color="primary" etc.

EXPECTED OUTPUT: Buttons, a card header, and icons all rendered in the
custom brand palette; changing the SCSS variables would re-skin the page.

CHECK: python3 check.py medium/p01

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <q-page class="q-pa-md">
    <!-- TODO: buttons, a card, and icons using brand colors -->
  </q-page>
</template>

<script setup>
// TODO: nothing required — colors come from the SCSS variable overrides
</script>
