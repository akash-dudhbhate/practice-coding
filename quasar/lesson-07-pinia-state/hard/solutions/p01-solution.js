/**
 * Complete auth store: useAuthStore
 * - user, token, isAuthenticated (getter)
 * - login (async), logout, persistence
 * - Error handling and loading state
 * Also includes a login form component.
 */
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

const STORAGE_KEY = 'auth_token'
const USER_KEY = 'auth_user'

export const useAuthStore = defineStore('auth', () => {
  // State
  const user = ref(loadUser())
  const token = ref(localStorage.getItem(STORAGE_KEY) || null)
  const loading = ref(false)
  const error = ref(null)

  // Getter: is the user authenticated?
  const isAuthenticated = computed(() => !!token.value)

  // Load saved user from localStorage
  function loadUser() {
    try {
      const saved = localStorage.getItem(USER_KEY)
      return saved ? JSON.parse(saved) : null
    } catch (e) {
      return null
    }
  }

  // Persist auth data to localStorage
  function persist() {
    if (token.value) {
      localStorage.setItem(STORAGE_KEY, token.value)
    } else {
      localStorage.removeItem(STORAGE_KEY)
    }
    if (user.value) {
      localStorage.setItem(USER_KEY, JSON.stringify(user.value))
    } else {
      localStorage.removeItem(USER_KEY)
    }
  }

  // Action: async login with error handling and loading state
  async function login(credentials) {
    loading.value = true
    error.value = null
    try {
      // Simulate API call
      await new Promise((resolve, reject) => {
        setTimeout(() => {
          if (credentials.email && credentials.password) {
            resolve({
              token: 'mock-jwt-token-' + Date.now(),
              user: { id: 1, name: 'Demo User', email: credentials.email },
            })
          } else {
            reject(new Error('Invalid credentials'))
          }
        }, 800)
      }).then((data) => {
        token.value = data.token
        user.value = data.user
        persist()
      })
    } catch (err) {
      error.value = err.message || 'Login failed'
      throw err
    } finally {
      loading.value = false
    }
  }

  // Action: logout and clear persistence
  function logout() {
    user.value = null
    token.value = null
    persist()
  }

  return {
    user,
    token,
    loading,
    error,
    isAuthenticated,
    login,
    logout,
  }
})

/*
 * Login form component:
 *
 * <template>
 *   <q-page class="q-pa-md">
 *     <q-card class="q-pa-lg" style="max-width: 400px; margin: 0 auto;">
 *       <q-card-section>
 *         <div class="text-h5">Login</div>
 *       </q-card-section>
 *       <q-card-section>
 *         <q-form @submit="handleLogin">
 *           <q-input v-model="form.email" label="Email" type="email" :rules="[v => !!v || 'Email required']" />
 *           <q-input v-model="form.password" label="Password" type="password"
 *             :rules="[v => !!v || 'Password required']" />
 *           <div v-if="error" class="text-negative q-mt-sm">{{ error }}</div>
 *           <q-btn type="submit" label="Login" color="primary" class="q-mt-md" :loading="loading" />
 *         </q-form>
 *       </q-card-section>
 *     </q-card>
 *   </q-page>
 * </template>
 *
 * <script setup>
 * import { ref } from 'vue'
 * import { useAuthStore } from './p01-solution.js'
 * import { storeToRefs } from 'pinia'
 *
 * const authStore = useAuthStore()
 * const { loading, error } = storeToRefs(authStore)
 * const { login } = authStore
 *
 * const form = ref({ email: '', password: '' })
 *
 * async function handleLogin() {
 *   try {
 *     await login(form.value)
 *     // Redirect on success
 *   } catch (e) {
 *     // Error is already in store
 *   }
 * }
 * </script>
 */
