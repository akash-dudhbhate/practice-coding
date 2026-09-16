<!--
LESSON 09 — Quasar Forms
EASY P02 — Select / Toggle / Checkbox / Radio
============================================
CONCEPT: Quasar's form controls all share v-model. q-select needs :options,
q-radio needs a `val` per option sharing one v-model, q-toggle/q-checkbox
bind booleans.

PROBLEM: A profile form with q-select (country), q-toggle (notifications),
q-checkbox (terms), and three q-radio options (gender). Show the live form
state as JSON below the form.

TRY THIS: <q-select v-model="form.country" :options="countries" />;
<q-radio v-model="form.gender" val="male" label="Male" />;
<pre>{{ JSON.stringify(form, null, 2) }}</pre>

EXPECTED OUTPUT: All four control types on one card; the JSON state updates
as you interact.

CHECK: python3 check.py easy/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
