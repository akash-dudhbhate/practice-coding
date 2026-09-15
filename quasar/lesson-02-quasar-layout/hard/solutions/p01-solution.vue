<!--
  Lesson 02 - Quasar Layout - Hard - Problem 01
  Header with reveal behavior (hides on scroll down, shows on scroll up).
  Toolbar with menu button, title, 2 action buttons.
-->
<template>
  <!--
    q-header `reveal` prop enables auto-hide:
    the header hides when scrolling down and reappears when scrolling up.
  -->
  <q-layout view="hHh lpR fFf">
    <q-header reveal elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn flat dense icon="menu" @click="drawer = !drawer" />
        <q-toolbar-title>Reveal Header</q-toolbar-title>

        <!-- Two action buttons in the toolbar -->
        <q-btn flat dense icon="search" />
        <q-btn flat dense icon="more_vert" />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="drawer" show-if-above bordered>
      <q-list>
        <q-item-label header>Menu</q-item-label>
        <q-item clickable v-ripple>
          <q-item-section avatar><q-icon name="home" /></q-item-section>
          <q-item-section>Home</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <!-- Tall page content so scrolling triggers the reveal behavior -->
      <q-page class="q-pa-md">
        <h2 class="text-h5">Scroll down to hide the header</h2>
        <p v-for="n in 50" :key="n" class="q-py-sm">
          Line {{ n }} — keep scrolling to see the header reveal behavior in action.
        </p>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

const drawer = ref(false)
</script>

<style scoped>
</style>
