<!--
  Lesson 02 - Quasar Layout - Hard - Problem 03
  Two layouts: MainLayout (header + drawer) and BlankLayout (just q-page-container).
  Route configuration is shown in comments below.

  --- Route configuration (src/router/routes.js) ---

  const routes = [
    {
      path: '/',
      component: () => import('layouts/MainLayout.vue'),
      children: [
        { path: '', component: () => import('pages/IndexPage.vue') },
        { path: 'dashboard', component: () => import('pages/DashboardPage.vue') },
      ],
    },
    {
      path: '/login',
      component: () => import('layouts/BlankLayout.vue'),
      children: [
        { path: '', component: () => import('pages/LoginPage.vue') },
      ],
    },
  ]

  Each layout wraps its child pages via <router-view /> inside q-page-container.
-->
<template>
  <!--
    This file demonstrates MainLayout.
    For BlankLayout, replace the template with the commented-out version below.

    --- BlankLayout template ---
    <q-layout view="hHh lpR fFf">
      <q-page-container>
        <router-view />
      </q-page-container>
    </q-layout>
  -->
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn flat dense icon="menu" @click="drawer = !drawer" />
        <q-toolbar-title>Main Layout</q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="drawer" show-if-above bordered>
      <q-list>
        <q-item-label header>Navigation</q-item-label>
        <q-item to="/" clickable v-ripple>
          <q-item-section avatar><q-icon name="home" /></q-item-section>
          <q-item-section>Home</q-item-section>
        </q-item>
        <q-item to="/dashboard" clickable v-ripple>
          <q-item-section avatar><q-icon name="dashboard" /></q-item-section>
          <q-item-section>Dashboard</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <!-- router-view renders the matched child page -->
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

const drawer = ref(true)
</script>

<style scoped>
</style>
