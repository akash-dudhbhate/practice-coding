<!--
  Desktop Settings App (Electron renderer)
  ----------------------------------------
  A settings panel that persists all preferences via Electron Store
  (exposed through the preload bridge as window.electronAPI.settings).

  Settings managed:
  - Window: size (width/height) and position (x/y) — restored on launch
  - Theme: dark or light — applied immediately
  - Startup: minimize to tray on close (boolean)
  - Auto-update: check for updates automatically (boolean)
  - Keyboard shortcuts: read-only reference list
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h4 q-mb-lg">Settings</div>

    <!-- Appearance -->
    <q-card flat bordered class="q-mb-md">
      <q-card-section>
        <div class="text-h6">Appearance</div>
      </q-card-section>
      <q-card-section class="q-pt-none">
        <div class="row items-center q-mb-sm">
          <q-icon name="dark_mode" class="q-mr-sm" />
          <q-toggle
            v-model="settings.darkMode"
            label="Dark mode"
            @update:model-value="saveAndApply"
          />
        </div>
      </q-card-section>
    </q-card>

    <!-- Window -->
    <q-card flat bordered class="q-mb-md">
      <q-card-section>
        <div class="text-h6">Window</div>
      </q-card-section>
      <q-card-section class="q-pt-none row q-col-gutter-md">
        <div class="col-6">
          <q-input
            v-model.number="settings.windowWidth"
            type="number"
            label="Width"
            outlined
            dense
            @update:model-value="save"
          />
        </div>
        <div class="col-6">
          <q-input
            v-model.number="settings.windowHeight"
            type="number"
            label="Height"
            outlined
            dense
            @update:model-value="save"
          />
        </div>
        <div class="col-6">
          <q-input
            v-model.number="settings.windowX"
            type="number"
            label="Position X"
            outlined
            dense
            @update:model-value="save"
          />
        </div>
        <div class="col-6">
          <q-input
            v-model.number="settings.windowY"
            type="number"
            label="Position Y"
            outlined
            dense
            @update:model-value="save"
          />
        </div>
      </q-card-section>
    </q-card>

    <!-- Startup behaviour -->
    <q-card flat bordered class="q-mb-md">
      <q-card-section>
        <div class="text-h6">Startup</div>
      </q-card-section>
      <q-card-section class="q-pt-none">
        <q-toggle
          v-model="settings.minimizeToTray"
          label="Minimize to tray on close"
          @update:model-value="save"
        />
        <q-toggle
          v-model="settings.autoUpdate"
          label="Check for updates automatically"
          class="q-mt-sm"
          @update:model-value="save"
        />
      </q-card-section>
    </q-card>

    <!-- Keyboard shortcuts reference -->
    <q-card flat bordered>
      <q-card-section>
        <div class="text-h6">Keyboard Shortcuts</div>
      </q-card-section>
      <q-list separator>
        <q-item v-for="sc in shortcuts" :key="sc.action">
          <q-item-section>{{ sc.action }}</q-item-section>
          <q-item-section side>
            <q-badge color="grey-7" :label="sc.keys" />
          </q-item-section>
        </q-item>
      </q-list>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Default settings — used when nothing is persisted yet
const defaultSettings = {
  darkMode: false,
  windowWidth: 1200,
  windowHeight: 800,
  windowX: 100,
  windowY: 100,
  minimizeToTray: true,
  autoUpdate: true,
}

const settings = ref({ ...defaultSettings })

// Static keyboard shortcuts reference
const shortcuts = [
  { action: 'Open File', keys: 'CmdOrCtrl+O' },
  { action: 'Save File', keys: 'CmdOrCtrl+S' },
  { action: 'Quit', keys: 'CmdOrCtrl+Q' },
  { action: 'Undo', keys: 'CmdOrCtrl+Z' },
  { action: 'Redo', keys: 'Shift+CmdOrCtrl+Z' },
  { action: 'Reload', keys: 'CmdOrCtrl+R' },
  { action: 'Toggle DevTools', keys: 'F12' },
  { action: 'Toggle Fullscreen', keys: 'F11' },
]

// ---- Lifecycle -----------------------------------------------------------
onMounted(async () => {
  await loadSettings()
})

// ---- Persistence ---------------------------------------------------------
/**
 * Load settings from Electron Store (via preload bridge) or fall back
 * to localStorage on the web.
 */
async function loadSettings() {
  try {
    if (window.electronAPI?.settings?.get) {
      const stored = await window.electronAPI.settings.get('app-settings')
      if (stored) {
        settings.value = { ...defaultSettings, ...JSON.parse(stored) }
      }
    } else {
      const stored = localStorage.getItem('app-settings')
      if (stored) {
        settings.value = { ...defaultSettings, ...JSON.parse(stored) }
      }
    }
    applyTheme()
  } catch {
    // ignore — use defaults
  }
}

/**
 * Persist the current settings.
 */
async function save() {
  const json = JSON.stringify(settings.value)
  try {
    if (window.electronAPI?.settings?.set) {
      await window.electronAPI.settings.set('app-settings', json)
    } else {
      localStorage.setItem('app-settings', json)
    }
  } catch {
    // ignore
  }
}

/**
 * Save and immediately apply the theme toggle.
 */
function saveAndApply() {
  save()
  applyTheme()
}

/**
 * Toggle Quasar's dark mode based on the setting.
 */
function applyTheme() {
  $q.dark.set(settings.value.darkMode)
}
</script>

<style scoped>
.q-page {
  max-width: 700px;
  margin: 0 auto;
}
</style>
