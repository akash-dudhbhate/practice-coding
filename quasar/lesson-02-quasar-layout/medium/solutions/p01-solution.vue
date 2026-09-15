<!--
  Lesson 02 - Quasar Layout - Medium - Problem 01
  Responsive layout: drawer with show-if-above, toggleable on mobile,
  breakpoint 1024px.
-->
<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <!-- On mobile the menu button toggles the drawer overlay -->
        <q-btn flat dense icon="menu" @click="drawer = !drawer" />
        <q-toolbar-title>Responsive Layout</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <!--
      show-if-above: drawer is always visible on screens wider than breakpoint.
      breakpoint: 1024 means below 1024px the drawer becomes an overlay.
    -->
    <q-drawer
      v-model="drawer"
      show-if-above
      :breakpoint="1024"
      bordered
    >
      <q-list>
        <q-item-label header>Navigation</q-item-label>
        <q-item clickable v-ripple>
          <q-item-section avatar><q-icon name="dashboard" /></q-item-section>
          <q-item-section>Dashboard</q-item-section>
        </q-item>
        <q-item clickable v-ripple>
          <q-item-section avatar><q-icon name="analytics" /></q-item-section>
          <q-item-section>Analytics</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <q-page class="flex flex-center">
        <p class="text-body1">
          Resize the browser window below 1024px to see the drawer switch
          to overlay mode.
        </p>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

// Drawer state; show-if-above handles large screens automatically
const drawer = ref(false)
</script>

<style scoped>
</style>
