<!--
  Lesson 02 - Quasar Layout - Easy - Problem 01
  Basic layout with q-layout, q-header (toolbar + title),
  q-page-container with q-page.
-->
<template>
  <!-- q-layout is the root wrapper for any Quasar app screen -->
  <q-layout view="hHh lpR fFf">
    <!-- q-header renders the top app bar -->
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-toolbar-title>My Quasar App</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <!-- q-page-container wraps the actual page content -->
    <q-page-container>
      <q-page class="flex flex-center">
        <p class="text-h6">Welcome to the home page!</p>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
// Static layout — no reactive state needed.
</script>

<style scoped>
/* The `view` prop "hHh lpR fFf" controls header/footer/drawer positioning */
</style>
