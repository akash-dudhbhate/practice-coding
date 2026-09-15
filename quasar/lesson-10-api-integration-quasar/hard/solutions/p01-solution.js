// Complete API layer: axios instance, interceptors, services, error handler, token refresh
import axios from 'axios'

// --- Centralized error handler ---
function handleError(error) {
  if (error.response) {
    const { status, data } = error.response
    console.error(`API Error ${status}:`, data)
    if (status === 401) console.warn('Unauthorized — token refresh needed')
    if (status === 404) console.warn('Resource not found')
    if (status >= 500) console.error('Server error')
  } else if (error.request) {
    console.error('No response received:', error.message)
  } else {
    console.error('Request setup error:', error.message)
  }
  return Promise.reject(error)
}

// --- Axios instance ---
const api = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
})

// --- Request interceptor: add auth token ---
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('auth_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  console.log(`[REQUEST] ${config.method?.toUpperCase()} ${config.url}`)
  return config
})

// --- Response interceptor: logging + error handling ---
let isRefreshing = false

api.interceptors.response.use(
  (response) => {
    console.log(`[RESPONSE] ${response.status} ${response.config.url}`)
    return response
  },
  async (error) => {
    const originalRequest = error.config

    // Token refresh on 401
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      if (!isRefreshing) {
        isRefreshing = true
        try {
          const refreshToken = localStorage.getItem('refresh_token')
          const res = await axios.post('https://api.example.com/refresh', { refreshToken })
          const newToken = res.data.token
          localStorage.setItem('auth_token', newToken)
          isRefreshing = false
          originalRequest.headers.Authorization = `Bearer ${newToken}`
          return api(originalRequest)
        } catch (refreshError) {
          isRefreshing = false
          localStorage.removeItem('auth_token')
          localStorage.removeItem('refresh_token')
          return handleError(refreshError)
        }
      }
    }

    return handleError(error)
  }
)

// --- User service ---
export const userService = {
  getAll: () => api.get('/users').then(r => r.data),
  getById: (id) => api.get(`/users/${id}`).then(r => r.data),
  create: (data) => api.post('/users', data).then(r => r.data),
  update: (id, data) => api.put(`/users/${id}`, data).then(r => r.data),
  remove: (id) => api.delete(`/users/${id}`).then(r => r.data),
}

// --- Post service ---
export const postService = {
  getAll: () => api.get('/posts').then(r => r.data),
  getById: (id) => api.get(`/posts/${id}`).then(r => r.data),
  create: (data) => api.post('/posts', data).then(r => r.data),
  update: (id, data) => api.put(`/posts/${id}`, data).then(r => r.data),
  remove: (id) => api.delete(`/posts/${id}`).then(r => r.data),
}

export default api
