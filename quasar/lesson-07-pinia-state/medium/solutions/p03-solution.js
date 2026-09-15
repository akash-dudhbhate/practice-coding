/**
 * useUserStore with localStorage persistence.
 * - Saves to localStorage on change (via watch)
 * - Loads from localStorage on init
 * - Clears on logout
 */
import { ref, watch } from 'vue'
import { defineStore } from 'pinia'

const STORAGE_KEY = 'app_user'

export const useUserStore = defineStore('user', () => {
  // Load initial state from localStorage
  const user = ref(loadFromStorage())

  // Load user from localStorage on init
  function loadFromStorage() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY)
      return saved ? JSON.parse(saved) : null
    } catch (e) {
      console.error('Failed to load user from storage:', e)
      return null
    }
  }

  // Save user to localStorage
  function saveToStorage(userData) {
    try {
      if (userData) {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(userData))
      } else {
        localStorage.removeItem(STORAGE_KEY)
      }
    } catch (e) {
      console.error('Failed to save user to storage:', e)
    }
  }

  // Watch for changes and auto-save to localStorage
  watch(
    user,
    (newUser) => {
      saveToStorage(newUser)
    },
    { deep: true }
  )

  // Action: login
  function login(userData) {
    user.value = { ...userData, id: Date.now() }
  }

  // Action: logout - clear user and localStorage
  function logout() {
    user.value = null
    // localStorage is cleared automatically via the watcher
  }

  return { user, login, logout }
})

/*
 * Component using the persistent user store:
 *
 * <template>
 *   <div class="q-pa-md">
 *     <div v-if="user">
 *       <p>Welcome back, {{ user.name }}!</p>
 *       <q-btn label="Logout" color="negative" @click="logout" />
 *     </div>
 *     <div v-else>
 *       <q-input v-model="name" label="Name" />
 *       <q-btn label="Login" color="primary" @click="login({ name })" />
 *     </div>
 *   </div>
 * </template>
 *
 * <script setup>
 * import { ref } from 'vue'
 * import { useUserStore } from './p03-solution.js'
 * import { storeToRefs } from 'pinia'
 *
 * const userStore = useUserStore()
 * const { user } = storeToRefs(userStore)
 * const { login, logout } = userStore
 *
 * const name = ref('')
 * </script>
 */
