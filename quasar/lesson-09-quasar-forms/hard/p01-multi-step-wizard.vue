<!--
LESSON 09 — Quasar Forms
HARD P01 — Multi-Step Form Wizard
============================================
CONCEPT: q-stepper + q-step gives step navigation with :done markers. Give
each step its own q-form ref; Next calls that form's .validate() and only
advances via stepperRef.next() when it passes.

PROBLEM: A 3-step wizard (Personal: name+email; Contact: phone+address;
Review: read-only summary list). Next validates the current step, Back goes
back, the last step shows Submit. Use q-stepper v-model="step" with a
#navigation slot.

TRY THIS: async function validateAndNext() {
  const f = step.value === 1 ? step1Form.value : step2Form.value;
  if (await f.validate()) stepperRef.value.next() }

EXPECTED OUTPUT: A stepper with Personal → Contact → Review; Next is blocked
by validation errors; Submit toasts success.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
