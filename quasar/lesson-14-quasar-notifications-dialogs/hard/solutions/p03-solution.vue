<template>
  <div class="q-pa-md">
    <q-btn flat round icon="notifications" @click="toggleDropdown">
      <q-badge v-if="unreadCount" color="negative" floating>{{ unreadCount }}</q-badge>
    </q-btn>

    <q-menu v-model="dropdownOpen" anchor="bottom right" self="top right">
      <q-card style="min-width: 320px">
        <q-card-section class="row items-center">
          <div class="text-h6">Notifications</div>
          <q-space />
          <q-btn flat dense label="Mark all read" @click="markAllRead" size="sm" />
        </q-card-section>
        <q-separator />
        <q-list style="max-height: 300px; overflow: auto">
          <q-item v-for="notif in notifications" :key="notif.id" clickable @click="markAsRead(notif)">
            <q-item-section avatar>
              <q-icon :name="iconForType(notif.type)" :color="colorForType(notif.type)" />
            </q-item-section>
            <q-item-section>
              <q-item-label :class="{ 'text-grey': notif.read }">{{ notif.message }}</q-item-label>
              <q-item-label caption>{{ notif.time }}</q-item-label>
            </q-item-section>
            <q-item-section side v-if="!notif.read">
              <q-badge color="primary" label="New" />
            </q-item-section>
          </q-item>
        </q-list>
      </q-card>
    </q-menu>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

const dropdownOpen = ref(false)

const notifications = ref([
  { id: 1, type: 'info', message: 'New feature available', time: '2m ago', read: false },
  { id: 2, type: 'warning', message: 'Storage almost full', time: '1h ago', read: false },
  { id: 3, type: 'error', message: 'Failed to sync data', time: '3h ago', read: false },
  { id: 4, type: 'info', message: 'Welcome to the app', time: '1d ago', read: true },
])

const unreadCount = computed(() => notifications.value.filter(n => !n.read).length)

// Persist read state to localStorage
watch(notifications, (val) => {
  const readState = val.reduce((acc, n) => { acc[n.id] = n.read; return acc }, {})
  localStorage.setItem('notif_read_state', JSON.stringify(readState))
}, { deep: true })

// Load read state from localStorage on mount
const saved = localStorage.getItem('notif_read_state')
if (saved) {
  try {
    const readState = JSON.parse(saved)
    notifications.value.forEach(n => { if (readState[n.id] !== undefined) n.read = readState[n.id] })
  } catch (e) { /* ignore */ }
}

function toggleDropdown() { dropdownOpen.value = !dropdownOpen.value }

function markAsRead(notif) {
  notif.read = true
}

function markAllRead() {
  notifications.value.forEach(n => { n.read = true })
}

function iconForType(type) {
  return { info: 'info', warning: 'warning', error: 'error' }[type] || 'info'
}

function colorForType(type) {
  return { info: 'primary', warning: 'warning', error: 'negative' }[type] || 'primary'
}
</script>
