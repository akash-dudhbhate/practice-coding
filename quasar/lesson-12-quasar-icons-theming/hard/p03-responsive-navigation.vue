<!--
PROBLEM: Responsive Navigation (Hard)
======================================

CONCEPT: Quasar visibility classes (gt-sm / lt-md) + QLayout with
header/footer tabs — desktop top bar vs. mobile bottom tabs.

TASK: Build a responsive navigation: top bar on desktop, bottom tabs on
mobile (use lt-md and gt-sm classes). Include icons and labels. Verify
it switches automatically on resize. Use Quasar's QLayout and QTabs.

TRY THIS:
- Wrap everything in q-layout with a view string
- Header (desktop): toolbar + tabs — hidden below the md breakpoint
- Footer (mobile): the same tabs — only shown below the md breakpoint
- Both tab sets share one activeTab ref so they stay in sync
- q-tab-panels can render per-tab content

EXPECTED OUTPUT: Wide window -> tabs in the top toolbar. Narrow window ->
tabs move to a bottom footer bar. Same 4 tabs (icons + labels) either way.

CHECK: python3 check.py hard/p03

TODO: Write your complete solution from scratch below.
      Remove this comment when done.
-->
<template>
  <!-- TODO: q-layout with responsive header (desktop) + footer (mobile) tabs -->
</template>

<script setup>
// TODO: one shared activeTab ref
</script>
