<!--
LESSON 01 — Quasar Basics
HARD P02 — Color Picker with Preview Card
============================================
CONCEPT: q-color is Quasar's color picker — v-model binds it to a
ref holding a hex string. A :style binding turns reactive data into
inline CSS, so a preview box can repaint live.

PROBLEM: Create a selectedColor ref (starting at e.g. '#1976d2')
bound to a <q-color v-model="selectedColor"> picker. Next to it, build a
<q-card> preview that displays the hex string with {{ selectedColor }}
and contains a preview box whose background is bound with
:style="{ backgroundColor: selectedColor }".

TRY THIS: pick a color — the hex text and the preview box update
instantly. Change the ref's initial value for a different starting
color.

EXPECTED OUTPUT: a color picker beside a card showing the selected
hex value and a box filled with that color.

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
