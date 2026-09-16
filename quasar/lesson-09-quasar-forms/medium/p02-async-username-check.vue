<!--
LESSON 09 — Quasar Forms
MEDIUM P02 — Async Username Availability
============================================
CONCEPT: Rules can be async, but watching the field yourself gives more
control: watch the username, set status 'checking', await a fake API call,
then set 'available' or 'taken'. Gate the submit button on the result.

PROBLEM: A username q-input (debounce ~500, :loading bound to `checking`,
required + min-length rules) plus a `status` ref ('idle'/'checking'/
'available'/'taken') driven by a watch that simulates an API with
setTimeout against a taken-usernames list. Status icons/messages shown;
submit disabled unless available.

TRY THIS: watch(username, async (val) => { status.value = 'checking';
  await new Promise(r => setTimeout(r, 800));
  status.value = taken.includes(val.toLowerCase()) ? 'taken' : 'available' })

EXPECTED OUTPUT: Typing 'admin' shows a spinner then "taken"; a fresh name
shows "available" and enables Submit.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
