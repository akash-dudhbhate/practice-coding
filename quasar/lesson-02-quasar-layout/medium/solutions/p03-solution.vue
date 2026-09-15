<!--
  Lesson 02 - Quasar Layout - Medium - Problem 03
  Layout with mini mode drawer.
  Header button toggles between mini (icons only) and full mode.
-->
<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <!-- Toggle between mini and full drawer mode -->
        <q-btn
          flat
          dense
          :icon="miniState ? 'chevron_right' : 'chevron_left'"
          @click="miniState = !miniState"
        />
        <q-toolbar-title>Mini Drawer Layout</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <!--
      mini: when true, drawer collapses to icon-only mode.
      :width controls the expanded width; mini-to-overlay handles the transition.
    -->
    <q-drawer
      v-model="drawer"
      show-if-above
      :mini="miniState"
      :width="250"
      :breakpoint="500"
      bordered
      @click.capture="miniState && (miniState = false)"
    >
      <q-list>
        <q-item-label v-if="!miniState" header>Navigation</q-item-label>
        <q-item clickable v-ripple>
          <q-item-section avatar><q-icon name="dashboard" /></q-item-section>
          <q-item-section>Dashboard</q-item-section>
        </q-item>
        <q-item clickable v-ripple>
          <q-item-section avatar><q-icon name="people" /></q-item-section>
          <q-item-section>Users</q-item-section>
        </q-item>
        <q-item clickable v-ripple>
          <q-item-section avatar><q-icon name="settings" /></q-item-section>
          <q-item-section>Settings</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <q-page class="flex flex-center">
        <p class="text-body1">
          Click the chevron in the header to toggle mini/full drawer mode.
          In mini mode, only icons are shown.
        </p>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

// Drawer open state
const drawer = ref(true)
// When true, drawer shrinks to icon-only width
const miniState = ref(true)
</script>

<style scoped>
</style>
