<!--
LESSON 09 — Quasar Forms
EASY P01 — Login Form with Validation
============================================
CONCEPT: q-input's :rules takes an array of functions — each returns true or
an error string. A q-btn with type="submit" inside q-form only fires @submit
when every rule passes.

PROBLEM: A login q-form with email (required + regex format) and password
(required + min 6 chars) inputs, a submit button, and an onSubmit that shows
the values in a $q.notify.

TRY THIS: :rules="[val => !!val || 'Email is required', val => /.+@.+\..+/.test(val) || 'Invalid email']"

EXPECTED OUTPUT: Submitting empty shows inline errors; valid input fires a
"Logged in with email: X" toast.

CHECK: python3 check.py easy/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
