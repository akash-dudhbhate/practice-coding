<template>
  <!-- beforeEach navigation guard display -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Navigation Guard</div>
        <div class="text-body1 q-mt-md">
          This file exports a beforeEach guard function. Import it in your router
          and call <code>router.beforeEach(guard)</code>.
        </div>
        <pre class="q-mt-md">{{ guardSource }}</pre>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
// Display the guard source for reference
const guardSource = `function beforeEachGuard(to, from, next) {
  const token = localStorage.getItem('token')
  const isAuthenticated = !!token

  // Route requires auth but user is not logged in
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ path: '/login', query: { redirect: to.fullPath } })
    return
  }

  // Route is guest-only but user is already logged in
  if (to.meta.guestOnly && isAuthenticated) {
    next({ path: '/dashboard' })
    return
  }

  next()
}`
</script>

<script>
// Export the guard function so it can be imported in router setup
export function beforeEachGuard(to, from, next) {
  const token = localStorage.getItem('token')
  const isAuthenticated = !!token

  // Route requires auth but user is not logged in
  if (to.meta.requiresAuth && !isAuthenticated) {
    next({ path: '/login', query: { redirect: to.fullPath } })
    return
  }

  // Route is guest-only but user is already logged in
  if (to.meta.guestOnly && isAuthenticated) {
    next({ path: '/dashboard' })
    return
  }

  next()
}
</script>

<style scoped>
pre {
  white-space: pre-wrap;
  word-break: break-word;
  font-size: 12px;
}
</style>
