<!--
LESSON 04 — Vue Composition API
HARD P02 — Reactive Form Validation
============================================
CONCEPT: reactive() holds the whole form in one object. A computed `isValid`
checks every rule at once; binding :disable="!isValid" gives you a
self-updating submit button. watch() lets you log validity flips.

PROBLEM: A registration form with reactive state { name, email, age, agree }.
q-input fields for name/email/age, a q-toggle for agree, a computed isValid
(name non-empty, email contains @, age > 0, agree true), a disabled-until-
valid Submit button, and a watch on isValid that logs changes.

TRY THIS: const form = reactive({ name: '', email: '', age: 0, agree: false });
const isValid = computed(() => form.name.trim() !== '' && form.email.includes('@') && form.age > 0 && form.agree)

EXPECTED OUTPUT: Four fields and a greyed-out Submit; filling everything
correctly enables it and flips the status text to "Form is valid!".

CHECK: python3 check.py hard/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
