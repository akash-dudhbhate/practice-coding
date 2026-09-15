<!--
  Lesson 12 - Hard - P02: White-Label Theme System
  Settings page with color pickers for primary, secondary, accent.
  Changes apply live via CSS variables, persist to localStorage.
  Reset to default button restores original colors.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">White-Label Theme Settings</div>

    <q-card flat bordered class="q-mb-md">
      <q-card-section>
        <div class="text-subtitle1 q-mb-md">Brand Colors</div>

        <!-- Color pickers for primary, secondary, accent -->
        <div class="row q-col-gutter-md">
          <div class="col-12 col-md-4">
            <div class="text-caption q-mb-sm">Primary Color</div>
            <q-input
              v-model="theme.primary"
              outlined
              dense
              @update:model-value="applyTheme"
            >
              <template #append>
                <q-icon name="colorize" :style="{ color: theme.primary }" />
              </template>
              <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                <q-color v-model="theme.primary" @update:model-value="applyTheme" />
              </q-popup-proxy>
            </q-input>
          </div>

          <div class="col-12 col-md-4">
            <div class="text-caption q-mb-sm">Secondary Color</div>
            <q-input
              v-model="theme.secondary"
              outlined
              dense
              @update:model-value="applyTheme"
            >
              <template #append>
                <q-icon name="colorize" :style="{ color: theme.secondary }" />
              </template>
              <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                <q-color v-model="theme.secondary" @update:model-value="applyTheme" />
              </q-popup-proxy>
            </q-input>
          </div>

          <div class="col-12 col-md-4">
            <div class="text-caption q-mb-sm">Accent Color</div>
            <q-input
              v-model="theme.accent"
              outlined
              dense
              @update:model-value="applyTheme"
            >
              <template #append>
                <q-icon name="colorize" :style="{ color: theme.accent }" />
              </template>
              <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                <q-color v-model="theme.accent" @update:model-value="applyTheme" />
              </q-popup-proxy>
            </q-input>
          </div>
        </div>

        <div class="q-mt-md q-gutter-sm">
          <q-btn color="negative" icon="restore" label="Reset to Default" no-caps @click="resetTheme" />
        </div>
      </q-card-section>
    </q-card>

    <!-- Live preview section -->
    <q-card flat bordered>
      <q-card-section class="bg-primary text-white" :style="{ backgroundColor: theme.primary }">
        <div class="text-h6">Live Preview</div>
      </q-card-section>
      <q-card-section class="q-gutter-md">
        <q-btn :style="{ backgroundColor: theme.primary, color: '#fff' }" label="Primary" no-caps />
        <q-btn :style="{ backgroundColor: theme.secondary, color: '#fff' }" label="Secondary" no-caps />
        <q-btn :style="{ backgroundColor: theme.accent, color: '#fff' }" label="Accent" no-caps />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { reactive, onMounted } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Default theme values
const defaultTheme = {
  primary: '#1976d2',
  secondary: '#26a69a',
  accent: '#9c27b0',
}

// Reactive theme object
const theme = reactive({ ...defaultTheme })

// Apply theme by setting CSS custom properties and persisting
function applyTheme() {
  document.documentElement.style.setProperty('--q-primary', theme.primary)
  document.documentElement.style.setProperty('--q-secondary', theme.secondary)
  document.documentElement.style.setProperty('--q-accent', theme.accent)
  localStorage.setItem('whitelabel-theme', JSON.stringify(theme))
}

// Reset to default colors
function resetTheme() {
  Object.assign(theme, defaultTheme)
  applyTheme()
  $q.notify({ type: 'info', message: 'Theme reset to default' })
}

// Restore saved theme on mount
onMounted(() => {
  const saved = localStorage.getItem('whitelabel-theme')
  if (saved) {
    Object.assign(theme, JSON.parse(saved))
    applyTheme()
  }
})
</script>

<style scoped>
</style>
