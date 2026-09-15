<!--
  Lesson 12 - Hard - P03: Responsive Navigation
  Top bar on desktop (gt-sm), bottom tabs on mobile (lt-md).
  Icons and labels for each tab. Auto-switches on resize.
  Uses QLayout and QTabs.
-->
<template>
  <q-layout view="hHh lpR fFf">
    <!-- Top navigation bar — visible on desktop (gt-sm) -->
    <q-header class="bg-primary text-white gt-sm">
      <q-toolbar>
        <q-icon name="apps" size="28px" class="q-mr-sm" />
        <q-toolbar-title>My App</q-toolbar-title>
        <q-tabs
          v-model="activeTab"
          inline-label
          class="bg-primary text-white"
        >
          <q-tab name="home" icon="home" label="Home" />
          <q-tab name="search" icon="search" label="Search" />
          <q-tab name="notifications" icon="notifications" label="Alerts" />
          <q-tab name="profile" icon="person" label="Profile" />
        </q-tabs>
      </q-toolbar>
    </q-header>

    <!-- Page content -->
    <q-page-container>
      <q-page class="q-pa-md">
        <div class="text-h5">Active Tab: {{ activeTab }}</div>

        <q-tab-panels v-model="activeTab" animated class="q-mt-md">
          <q-tab-panel name="home">
            <div class="text-h6">Home</div>
            <p>Welcome to the home page. On desktop you see a top bar; on mobile, bottom tabs.</p>
          </q-tab-panel>
          <q-tab-panel name="search">
            <div class="text-h6">Search</div>
            <q-input outlined placeholder="Search..." dense>
              <template #prepend><q-icon name="search" /></template>
            </q-input>
          </q-tab-panel>
          <q-tab-panel name="notifications">
            <div class="text-h6">Alerts</div>
            <p>You have 3 new notifications.</p>
          </q-tab-panel>
          <q-tab-panel name="profile">
            <div class="text-h6">Profile</div>
            <p>User profile settings and preferences.</p>
          </q-tab-panel>
        </q-tab-panels>
      </q-page>
    </q-page-container>

    <!-- Bottom navigation tabs — visible on mobile (lt-md) -->
    <q-footer class="bg-primary lt-md">
      <q-tabs
        v-model="activeTab"
        dense
        active-color="white"
        indicator-color="white"
        class="text-white"
      >
        <q-tab name="home" icon="home" label="Home" />
        <q-tab name="search" icon="search" label="Search" />
        <q-tab name="notifications" icon="notifications" label="Alerts" />
        <q-tab name="profile" icon="person" label="Profile" />
      </q-tabs>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

// Shared active tab state — works for both top bar and bottom tabs
const activeTab = ref('home')
</script>

<style scoped>
/* gt-sm: visible on screens > 1024px (desktop) */
/* lt-md: visible on screens < 768px (mobile) */
/* Quasar handles the responsive visibility automatically via these classes */
</style>
