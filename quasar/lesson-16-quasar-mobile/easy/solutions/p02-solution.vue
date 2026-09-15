<!--
  Responsive Layout — Adaptive Navigation
  -----------------------------------------
  Shows a left drawer (QDrawer) on desktop and bottom tabs (QTabPanels +
  QTabs) on mobile. The choice is driven by $q.platform.is.mobile and
  $q.platform.is.desktop so the correct navigation appears automatically
  on each device class.
-->
<template>
  <q-layout view="hHh lpR fFf">
    <!-- Header bar common to both layouts -->
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn
          v-if="$q.platform.is.desktop"
          flat
          round
          dense
          icon="menu"
          @click="drawer = !drawer"
        />
        <q-toolbar-title>Adaptive Nav App</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <!-- Desktop: left drawer with navigation list -->
    <q-drawer
      v-if="$q.platform.is.desktop"
      v-model="drawer"
      show-if-above
      side="left"
      bordered
      :width="240"
    >
      <q-list padding>
        <q-item-label header>Navigation</q-item-label>
        <q-item
          v-for="item in navItems"
          :key="item.name"
          clickable
          :active="activeTab === item.name"
          @click="activeTab = item.name"
        >
          <q-item-section avatar>
            <q-icon :name="item.icon" />
          </q-item-section>
          <q-item-section>{{ item.label }}</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <!-- Main content area -->
    <q-page-container>
      <q-page padding>
        <div class="text-h6">Current page: {{ activeTab }}</div>
        <p class="text-grey-7">
          Detected as {{ $q.platform.is.mobile ? 'mobile' : 'desktop' }}
        </p>
      </q-page>
    </q-page-container>

    <!-- Mobile: bottom tab bar -->
    <q-footer
      v-if="$q.platform.is.mobile"
      elevated
      class="bg-primary text-white"
    >
      <q-tabs
        v-model="activeTab"
        dense
        align="justify"
      >
        <q-tab
          v-for="item in navItems"
          :key="item.name"
          :name="item.name"
          :icon="item.icon"
          :label="item.label"
        />
      </q-tabs>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

// Drawer open state (desktop only)
const drawer = ref(true)

// Currently active navigation tab
const activeTab = ref('home')

// Three navigation items shared by both layouts
const navItems = [
  { name: 'home', label: 'Home', icon: 'home' },
  { name: 'search', label: 'Search', icon: 'search' },
  { name: 'profile', label: 'Profile', icon: 'person' },
]
</script>

<style scoped>
/* Ensure the bottom tab labels stay readable on small screens */
.q-tab__label {
  font-size: 11px;
}
</style>
