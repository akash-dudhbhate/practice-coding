<!--
LESSON 06 — Vue Router in Quasar
MEDIUM P03 — Named Route Links
============================================
CONCEPT: Named routes decouple links from URLs — :to="{ name: 'UserDetail',
params: { id: user.id } }" navigates even if the path pattern changes later.
q-btn accepts `to` just like router-link.

PROBLEM: A user list page. 5 mock users ({ id, name, email }) rendered in a
q-list, each row showing name + email plus a q-btn "View Details" using a
named route with params.

TRY THIS: <q-btn :to="{ name: 'UserDetail', params: { id: user.id } }" label="View Details" />

EXPECTED OUTPUT: A list of 5 users; each has a button that would navigate to
that user's detail route.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
