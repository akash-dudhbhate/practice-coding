<!--
  Lesson 12 - Medium - P03: Theme Switcher
  3 theme buttons (blue, green, purple) that change --q-primary and
  --q-secondary CSS variables dynamically. Selection persists to localStorage.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Theme Switcher</div>

    <!-- Theme selection buttons -->
    <div class="q-mb-md q-gutter-sm">
      <q-btn
        v-for="theme in themes"
        :key="theme.name"
        :label="theme.label"
        :style="{ backgroundColor: theme.primary, color: '#fff' }"
        no-caps
        :outline="currentTheme !== theme.name"
        @click="applyTheme(theme)"
      />
    </div>

    <!-- Preview components that reflect the current theme -->
    <q-card flat bordered class="q-mb-md">
      <q-card-section class="bg-primary text-white">
        <div class="text-h6">Theme Preview</div>
        <div class="text-subtitle2">Primary color applied here</div>
      </q-card-section>
      <q-card-section>
        <q-btn color="primary" label="Primary Button" no-caps class="q-mr-sm" />
        <q-btn color="secondary" label="Secondary Button" no-caps />
      </q-card-section>
    </q-card>

    <q-banner class="bg-blue-1 text-blue-8">
      <template #avatar>
        <q-icon name="info" />
      </template>
      Current theme: {{ currentTheme }}. Selection saved to localStorage.
    </q-banner>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// Available themes with primary and secondary color values
const themes = [
  { name: 'blue', label: 'Blue', primary: '#1976d2', secondary: '#26a69a' },
  { name: 'green', label: 'Green', primary: '#2e7d32', secondary: '#ff9800' },
  { name: 'purple', label: 'Purple', primary: '#7b1fa2', secondary: '#e91e63' },
]

const currentTheme = ref('blue')

// Apply theme by setting CSS custom properties on document root
function applyTheme(theme) {
  currentTheme.value = theme.name
  document.documentElement.style.setProperty('--q-primary', theme.primary)
  document.documentElement.style.setProperty('--q-secondary', theme.secondary)
  // Persist to localStorage
  localStorage.setItem('app-theme', JSON.stringify(theme))
}

// Restore saved theme on mount
onMounted(() => {
  const saved = localStorage.getItem('app-theme')
  if (saved) {
    const theme = JSON.parse(saved)
    applyTheme(theme)
  }
})
</script>

<style scoped>
</style>
