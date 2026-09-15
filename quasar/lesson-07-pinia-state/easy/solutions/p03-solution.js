/**
 * useThemeStore: dark mode toggle store
 * Also includes a component that uses $q.dark.set() to apply the theme.
 */
import { ref } from 'vue'
import { defineStore } from 'pinia'

// Store definition
export const useThemeStore = defineStore('theme', () => {
  // State: dark mode boolean
  const dark = ref(false)

  // Action: toggle dark mode
  function toggle() {
    dark.value = !dark.value
  }

  // Action: set dark mode explicitly
  function setDark(value) {
    dark.value = value
  }

  return {
    dark,
    toggle,
    setDark,
  }
})

/*
 * Component using the theme store with $q.dark.set():
 *
 * <template>
 *   <div class="q-pa-md">
 *     <q-toggle
 *       v-model="dark"
 *       label="Dark Mode"
 *       @update:model-value="applyTheme"
 *     />
 *     <p>Dark mode is: {{ dark ? 'ON' : 'OFF' }}</p>
 *   </div>
 * </template>
 *
 * <script setup>
 * import { useThemeStore } from './p03-solution.js'
 * import { storeToRefs } from 'pinia'
 * import { useQuasar } from 'quasar'
 *
 * const $q = useQuasar()
 * const themeStore = useThemeStore()
 * const { dark } = storeToRefs(themeStore)
 *
 * // Apply dark mode using Quasar's $q.dark.set()
 * function applyTheme(value) {
 *   $q.dark.set(value)
 * }
 *
 * // Initialize from store on mount
 * $q.dark.set(dark.value)
 * </script>
 */
