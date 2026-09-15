<!--
  Mobile-Aware App Shell
  ----------------------
  - Detects the runtime platform (web / iOS / Android) via $q.platform
  - Adapts the layout: bottom tabs on mobile, left drawer on desktop
  - Triggers haptic feedback on button presses (mobile only)
  - Applies safe-area insets so content is not hidden behind notches or home bars
  - Platform-specific styling (e.g. iOS-style list separators)
-->
<template>
  <q-layout view="hHh lpR fFf" :class="platformClass">
    <!-- Header -->
    <q-header elevated class="bg-primary text-white safe-area-top">
      <q-toolbar>
        <q-btn
          v-if="isDesktop"
          flat
          round
          dense
          icon="menu"
          @click="hapticTap(() => (drawer = !drawer))"
        />
        <q-toolbar-title>
          <q-icon :name="platformIcon" class="q-mr-sm" />
          {{ platformLabel }} Shell
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <!-- Desktop drawer -->
    <q-drawer
      v-if="isDesktop"
      v-model="drawer"
      show-if-above
      bordered
      :width="240"
    >
      <q-list padding>
        <q-item-label header>Menu</q-item-label>
        <q-item
          v-for="item in navItems"
          :key="item.name"
          clickable
          :active="activeTab === item.name"
          @click="hapticTap(() => (activeTab = item.name))"
        >
          <q-item-section avatar><q-icon :name="item.icon" /></q-item-section>
          <q-item-section>{{ item.label }}</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <!-- Page content -->
    <q-page-container class="safe-area-content">
      <q-page padding>
        <div class="text-h6">Active: {{ activeTab }}</div>
        <p class="text-grey-7">
          Running on <b>{{ platformLabel }}</b>
        </p>

        <!-- Demo buttons that trigger haptics on mobile -->
        <div class="row q-gutter-sm q-mt-md">
          <q-btn
            v-for="item in navItems"
            :key="item.name"
            :color="activeTab === item.name ? 'primary' : 'grey-4'"
            :text-color="activeTab === item.name ? 'white' : 'dark'"
            :icon="item.icon"
            :label="item.label"
            @click="hapticTap(() => (activeTab = item.name))"
          />
        </div>
      </q-page>
    </q-page-container>

    <!-- Mobile bottom tabs -->
    <q-footer
      v-if="!isDesktop"
      elevated
      class="bg-primary text-white safe-area-bottom"
    >
      <q-tabs v-model="activeTab" dense align="justify">
        <q-tab
          v-for="item in navItems"
          :key="item.name"
          :name="item.name"
          :icon="item.icon"
          :label="item.label"
          @click="hapticTap(() => {})"
        />
      </q-tabs>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const drawer = ref(true)
const activeTab = ref('home')

const navItems = [
  { name: 'home', label: 'Home', icon: 'home' },
  { name: 'search', label: 'Search', icon: 'search' },
  { name: 'profile', label: 'Profile', icon: 'person' },
]

// ---- Platform detection --------------------------------------------------
const isDesktop = computed(() => $q.platform.is.desktop)

const platformLabel = computed(() => {
  if ($q.platform.is.ios) return 'iOS'
  if ($q.platform.is.android) return 'Android'
  return 'Web'
})

const platformClass = computed(() => {
  if ($q.platform.is.ios) return 'platform-ios'
  if ($q.platform.is.android) return 'platform-android'
  return 'platform-web'
})

const platformIcon = computed(() => {
  if ($q.platform.is.ios) return 'apple'
  if ($q.platform.is.android) return 'android'
  return 'language'
})

// ---- Haptics -------------------------------------------------------------
/**
 * Execute a callback and fire haptic feedback on mobile devices.
 * On web this is a plain pass-through.
 */
async function hapticTap(callback) {
  callback()

  if (!$q.platform.is.capacitor) return

  try {
    const { Haptics, ImpactStyle } = await import('@capacitor/haptics')
    await Haptics.impact({ style: ImpactStyle.Light })
  } catch {
    // Haptics plugin not available — silently ignore
  }
}
</script>

<style scoped>
/* Safe-area insets so content avoids notches and home indicators */
.safe-area-top {
  padding-top: env(safe-area-inset-top);
}
.safe-area-bottom {
  padding-bottom: env(safe-area-inset-bottom);
}
.safe-area-content {
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}

/* Platform-specific tweaks */
.platform-ios .q-tab__label {
  font-size: 10px; /* iOS uses smaller tab labels */
}
.platform-android .q-btn {
  text-transform: none; /* Android avoids ALL CAPS */
}
</style>
