<!--
  Lesson 02 - Quasar Layout - Easy - Problem 02
  Left drawer with navigation list (Home, About, Contact)
  and a toggle button in the header.
-->
<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <!-- Toggle button flips the drawer open/closed -->
        <q-btn flat dense icon="menu" @click="drawer = !drawer" />
        <q-toolbar-title>Navigation Demo</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <!-- Left navigation drawer -->
    <q-drawer v-model="drawer" show-if-above bordered>
      <q-list>
        <q-item-label header>Menu</q-item-label>

        <q-item
          v-for="item in navItems"
          :key="item.label"
          clickable
          v-ripple
        >
          <q-item-section avatar>
            <q-icon :name="item.icon" />
          </q-item-section>
          <q-item-section>{{ item.label }}</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <q-page class="flex flex-center">
        <p class="text-h6">Main content area</p>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

// Drawer visibility state
const drawer = ref(true)

// Navigation items shown in the drawer
const navItems = [
  { label: 'Home', icon: 'home' },
  { label: 'About', icon: 'info' },
  { label: 'Contact', icon: 'mail' },
]
</script>

<style scoped>
</style>
