<!--
  Lesson 02 - Quasar Layout - Medium - Problem 02
  Layout with both left and right drawers.
  Left = nav menu, Right = notifications panel.
  Both toggleable from header.
-->
<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <!-- Toggle left drawer -->
        <q-btn flat dense icon="menu" @click="leftDrawer = !leftDrawer" />
        <q-toolbar-title>Dual Drawers</q-toolbar-title>
        <!-- Toggle right drawer -->
        <q-btn flat dense icon="notifications" @click="rightDrawer = !rightDrawer" />
      </q-toolbar>
    </q-header>

    <!-- Left drawer: navigation menu -->
    <q-drawer v-model="leftDrawer" show-if-above bordered side="left">
      <q-list>
        <q-item-label header>Menu</q-item-label>
        <q-item clickable v-ripple>
          <q-item-section avatar><q-icon name="home" /></q-item-section>
          <q-item-section>Home</q-item-section>
        </q-item>
        <q-item clickable v-ripple>
          <q-item-section avatar><q-icon name="info" /></q-item-section>
          <q-item-section>About</q-item-section>
        </q-item>
        <q-item clickable v-ripple>
          <q-item-section avatar><q-icon name="mail" /></q-item-section>
          <q-item-section>Contact</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <!-- Right drawer: notifications panel -->
    <q-drawer v-model="rightDrawer" show-if-above bordered side="right" :width="300">
      <q-list>
        <q-item-label header>Notifications</q-item-label>
        <q-item v-for="note in notifications" :key="note.id">
          <q-item-section avatar>
            <q-icon :name="note.icon" :color="note.color" />
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ note.title }}</q-item-label>
            <q-item-label caption>{{ note.time }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <q-page class="flex flex-center">
        <p class="text-body1">Main content — toggle both drawers from the header.</p>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

// Left drawer (nav) visibility
const leftDrawer = ref(true)
// Right drawer (notifications) visibility
const rightDrawer = ref(false)

// Sample notifications data
const notifications = ref([
  { id: 1, title: 'New message from Alice', time: '2 min ago', icon: 'chat', color: 'primary' },
  { id: 2, title: 'Server backup complete', time: '1 hour ago', icon: 'backup', color: 'positive' },
  { id: 3, title: 'Low disk space warning', time: '3 hours ago', icon: 'warning', color: 'warning' },
])
</script>

<style scoped>
</style>
