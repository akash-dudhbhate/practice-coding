<!--
  Lesson 02 - Quasar Layout - Hard - Problem 02
  Complete admin layout: header with user avatar,
  left drawer with collapsible nav sections (Dashboard, Users, Settings
  with sub-items), footer with status.
-->
<template>
  <q-layout view="hHh lpR fFf">
    <!-- Header with user avatar -->
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn flat dense icon="menu" @click="drawer = !drawer" />
        <q-toolbar-title>Admin Panel</q-toolbar-title>

        <!-- User avatar with dropdown -->
        <q-avatar size="36px" class="cursor-pointer">
          <img src="https://cdn.quasar.dev/img/avatar.png" alt="avatar" />
          <q-menu>
            <q-list style="min-width: 150px">
              <q-item clickable v-close-popup>
                <q-item-section avatar><q-icon name="person" /></q-item-section>
                <q-item-section>Profile</q-item-section>
              </q-item>
              <q-item clickable v-close-popup>
                <q-item-section avatar><q-icon name="logout" /></q-item-section>
                <q-item-section>Logout</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-avatar>
      </q-toolbar>
    </q-header>

    <!-- Left drawer with collapsible nav sections -->
    <q-drawer v-model="drawer" show-if-above bordered :width="260">
      <q-list>
        <q-item-label header>Admin Navigation</q-item-label>

        <!-- Dashboard (simple link, no children) -->
        <q-item clickable v-ripple>
          <q-item-section avatar><q-icon name="dashboard" /></q-item-section>
          <q-item-section>Dashboard</q-item-section>
        </q-item>

        <!-- Users section with collapsible sub-items -->
        <q-expansion-item icon="people" label="Users">
          <q-item clickable v-ripple inset>
            <q-item-section>All Users</q-item-section>
          </q-item>
          <q-item clickable v-ripple inset>
            <q-item-section>Add User</q-item-section>
          </q-item>
          <q-item clickable v-ripple inset>
            <q-item-section>Roles</q-item-section>
          </q-item>
        </q-expansion-item>

        <!-- Settings section with collapsible sub-items -->
        <q-expansion-item icon="settings" label="Settings">
          <q-item clickable v-ripple inset>
            <q-item-section>General</q-item-section>
          </q-item>
          <q-item clickable v-ripple inset>
            <q-item-section>Security</q-item-section>
          </q-item>
          <q-item clickable v-ripple inset>
            <q-item-section>Notifications</q-item-section>
          </q-item>
        </q-expansion-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <q-page class="q-pa-md">
        <h2 class="text-h5">Admin Dashboard</h2>
        <p>Welcome back, admin! Use the left drawer to navigate.</p>
      </q-page>
    </q-page-container>

    <!-- Footer with status -->
    <q-footer elevated class="bg-grey-9 text-white">
      <q-toolbar>
        <q-icon name="wifi" class="q-mr-sm" />
        <q-toolbar-title class="text-caption">
          System Status: All services operational
        </q-toolbar-title>
        <span class="text-caption">v1.0.0</span>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

const drawer = ref(true)
</script>

<style scoped>
</style>
