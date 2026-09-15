<!--
  Lesson 02 - Quasar Layout - Easy - Problem 03
  Footer with 3 q-tabs (Home, Search, Settings) below page container.
-->
<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-toolbar-title>Tabs in Footer</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <q-page class="flex flex-center">
        <p class="text-h6">Page content goes here</p>
      </q-page>
    </q-page-container>

    <!-- q-footer sits at the bottom; q-tabs inside it -->
    <q-footer elevated class="bg-grey-9 text-white">
      <q-tabs v-model="activeTab" align="justify">
        <q-tab name="home" icon="home" label="Home" />
        <q-tab name="search" icon="search" label="Search" />
        <q-tab name="settings" icon="settings" label="Settings" />
      </q-tabs>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

// Tracks which footer tab is currently active
const activeTab = ref('home')
</script>

<style scoped>
</style>
