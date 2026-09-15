<template>
  <!-- Platform-aware component: mobile = bottom sheet, desktop = dropdown menu -->
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Platform-Aware Menu</div>
    <div class="text-subtitle1 q-mb-md">
      Platform: <q-badge color="primary">{{ isMobile ? 'Mobile' : 'Desktop' }}</q-badge>
      Screen: <q-badge color="secondary">{{ $q.screen.name }}</q-badge>
    </div>

    <!-- Desktop: dropdown menu -->
    <q-btn
      v-if="!isMobile"
      label="Open Menu"
      color="primary"
      icon="menu"
    >
      <q-menu>
        <q-list style="min-width: 200px">
          <q-item v-for="item in menuItems" :key="item.label" clickable v-close-popup @click="handleSelect(item)">
            <q-item-section avatar>
              <q-icon :name="item.icon" />
            </q-item-section>
            <q-item-section>{{ item.label }}</q-item-section>
          </q-item>
        </q-list>
      </q-menu>
    </q-btn>

    <!-- Mobile: bottom sheet menu -->
    <q-btn
      v-else
      label="Open Menu"
      color="primary"
      icon="menu"
      @click="openBottomSheet"
    />
  </q-page>
</template>

<script setup>
import { computed } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Detect if mobile using $q.platform and $q.screen
const isMobile = computed(() => $q.platform.is.mobile || $q.screen.xs)

// Menu items (4+)
const menuItems = [
  { label: 'Profile', icon: 'person' },
  { label: 'Settings', icon: 'settings' },
  { label: 'Messages', icon: 'message' },
  { label: 'Help', icon: 'help' },
  { label: 'Logout', icon: 'logout' },
]

// Handle menu item selection
function handleSelect(item) {
  $q.notify({ type: 'info', message: `Selected: ${item.label}` })
}

// Open bottom sheet for mobile using $q.bottomSheet
function openBottomSheet() {
  $q.bottomSheet({
    title: 'Menu',
    actions: menuItems.map((item) => ({
      label: item.label,
      icon: item.icon,
      id: item.label,
    })),
  }).onOk((action) => {
    $q.notify({ type: 'info', message: `Selected: ${action.label}` })
  })
}
</script>

<style scoped>
.q-page {
  max-width: 500px;
  margin: 0 auto;
}
</style>
