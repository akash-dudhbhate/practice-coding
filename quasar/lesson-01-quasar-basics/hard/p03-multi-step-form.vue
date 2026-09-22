<!--
LESSON 01 — Quasar Basics
HARD P03 — Multi-Step Form Wizard
============================================
CONCEPT: A step ref plus v-if per step renders one section at a
time — the classic wizard pattern. One reactive form object collects
fields across every step.

PROBLEM: Create a step ref (1-3) and a form ref ({ name, email,
address, city }). Render THREE step blocks, each gated by v-if:
step 1 = name + email <q-input>s, step 2 = address + city <q-input>s
(all v-model'd into form), step 3 = a review list of the entered
values. Add navigation <q-btn>s — Back (:disable="step === 1"), Next
(v-if="step < 3", @click="step++"), and Submit (v-else, calls an
onSubmit handler). A "Step {{ step }} of 3" line is a nice touch.

TRY THIS: fill step 1, click Next — the fields swap. On step 3 the
review shows everything you typed, and Submit fires your handler
(e.g. alert the form data).

EXPECTED OUTPUT: a 3-step wizard — each step shows only its own
fields, Back/Next navigate, Submit finishes on the review step.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
