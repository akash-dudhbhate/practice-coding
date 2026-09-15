<!--
  Lesson 03 - Quasar Components - Easy - Problem 02
  q-list with 3 q-items, each with avatar icon, label, caption,
  and side badge showing status.
-->
<template>
  <q-page class="flex flex-center" style="max-width: 400px; margin: 0 auto;">
    <q-list bordered separator class="full-width">
      <q-item v-for="user in users" :key="user.id" clickable v-ripple>
        <!-- Avatar icon -->
        <q-item-section avatar>
          <q-icon :name="user.icon" :color="user.iconColor" size="32px" />
        </q-item-section>

        <!-- Label and caption -->
        <q-item-section>
          <q-item-label>{{ user.name }}</q-item-label>
          <q-item-label caption>{{ user.email }}</q-item-label>
        </q-item-section>

        <!-- Side badge showing status -->
        <q-item-section side>
          <q-badge
            :color="user.statusColor"
            :label="user.status"
            class="q-pa-sm"
          />
        </q-item-section>
      </q-item>
    </q-list>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Sample user data with status badges
const users = ref([
  { id: 1, name: 'Alice Johnson', email: 'alice@example.com', icon: 'person', iconColor: 'primary', status: 'Online', statusColor: 'green' },
  { id: 2, name: 'Bob Smith', email: 'bob@example.com', icon: 'person', iconColor: 'orange', status: 'Away', statusColor: 'orange' },
  { id: 3, name: 'Carol White', email: 'carol@example.com', icon: 'person', iconColor: 'grey', status: 'Offline', statusColor: 'grey' },
])
</script>

<style scoped>
</style>
