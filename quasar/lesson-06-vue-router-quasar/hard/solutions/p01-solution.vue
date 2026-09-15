<template>
  <!-- Full route config with nested routes display -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Full Route Configuration</div>
        <pre>{{ JSON.stringify(routes, null, 2) }}</pre>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
// Full route config with nested routes:
// MainLayout with children (Home, Dashboard, Settings)
// BlankLayout with children (Login, Register)
// meta: { requiresAuth: true } on Dashboard/Settings
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import('pages/HomePage.vue'),
        meta: { title: 'Home' },
      },
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: () => import('pages/DashboardPage.vue'),
        meta: { title: 'Dashboard', requiresAuth: true },
      },
      {
        path: 'settings',
        name: 'Settings',
        component: () => import('pages/SettingsPage.vue'),
        meta: { title: 'Settings', requiresAuth: true },
      },
    ],
  },
  {
    path: '/',
    component: () => import('layouts/BlankLayout.vue'),
    children: [
      {
        path: 'login',
        name: 'Login',
        component: () => import('pages/LoginPage.vue'),
        meta: { title: 'Login', guestOnly: true },
      },
      {
        path: 'register',
        name: 'Register',
        component: () => import('pages/RegisterPage.vue'),
        meta: { title: 'Register', guestOnly: true },
      },
    ],
  },
]
</script>

<style scoped>
pre {
  white-space: pre-wrap;
  word-break: break-word;
  font-size: 12px;
}
</style>
