<template>
  <!-- Settings panel: dark mode, notification position, language, screen size - all persisted -->
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Settings Panel</div>
    <q-card class="q-pa-lg">
      <!-- Dark Mode Toggle -->
      <q-card-section>
        <div class="text-h6">Appearance</div>
        <q-toggle
          v-model="settings.darkMode"
          label="Dark Mode"
          @update:model-value="applyDarkMode"
        />
      </q-card-section>

      <q-separator />

      <!-- Notification Position Selector -->
      <q-card-section>
        <div class="text-h6">Notification Position</div>
        <q-btn-dropdown :label="settings.notifyPosition" color="primary" class="q-mt-sm">
          <q-list>
            <q-item
              v-for="pos in positions"
              :key="pos"
              clickable
              v-close-popup
              @click="setNotifyPosition(pos)"
            >
              <q-item-section>{{ pos }}</q-item-section>
            </q-item>
          </q-list>
        </q-btn-dropdown>
        <q-btn label="Test Notification" color="secondary" class="q-ml-sm q-mt-sm" @click="testNotification" />
      </q-card-section>

      <q-separator />

      <!-- Language Selector -->
      <q-card-section>
        <div class="text-h6">Language</div>
        <q-select
          v-model="settings.language"
          :options="languages"
          label="Select Language"
          style="max-width: 250px"
          @update:model-value="saveSettings"
        />
      </q-card-section>

      <q-separator />

      <!-- Screen Size Display -->
      <q-card-section>
        <div class="text-h6">Screen Information</div>
        <p>Breakpoint: <strong>{{ $q.screen.name }}</strong></p>
        <p>Width: <strong>{{ $q.screen.width }}px</strong></p>
        <p>Height: <strong>{{ $q.screen.height }}px</strong></p>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { reactive, onMounted } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const STORAGE_KEY = 'app_settings'

// Available notification positions
const positions = [
  'top', 'top-left', 'top-right', 'top-center',
  'bottom', 'bottom-left', 'bottom-right', 'bottom-center',
  'left', 'right', 'center',
]

// Available languages
const languages = ['English', 'Spanish', 'French', 'German', 'Japanese']

// Settings state (persisted to localStorage)
const settings = reactive({
  darkMode: false,
  notifyPosition: 'top-right',
  language: 'English',
})

// Load settings from localStorage on mount
onMounted(() => {
  loadSettings()
  applyDarkMode(settings.darkMode)
})

function loadSettings() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY)
    if (saved) {
      const parsed = JSON.parse(saved)
      Object.assign(settings, parsed)
    }
  } catch (e) {
    console.error('Failed to load settings:', e)
  }
}

// Save settings to localStorage
function saveSettings() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(settings))
  } catch (e) {
    console.error('Failed to save settings:', e)
  }
}

// Apply dark mode and persist
function applyDarkMode(value) {
  $q.dark.set(value)
  saveSettings()
}

// Set notification position and persist
function setNotifyPosition(pos) {
  settings.notifyPosition = pos
  saveSettings()
}

// Test notification at the selected position
function testNotification() {
  $q.notify({
    type: 'info',
    message: `Notification at ${settings.notifyPosition}`,
    position: settings.notifyPosition,
    timeout: 3000,
  })
}
</script>

<style scoped>
.q-card {
  max-width: 600px;
  margin: 0 auto;
}
</style>
