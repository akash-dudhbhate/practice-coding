<!--
  Lesson 13 - Medium - P03: Page Route Transition
  <Transition> with mode="out-in" around <router-view>.
  Slide-fade transition between 3 pages. Requires vue-router setup.

  --- Router setup (src/router/routes.js) ---
  const routes = [
    { path: '/', component: () => import('pages/PageHome.vue') },
    { path: '/about', component: () => import('pages/PageAbout.vue') },
    { path: '/contact', component: () => import('pages/PageContact.vue') },
  ]
  ---
-->
<template>
  <q-page class="q-pa-md">
    <!-- Navigation links for the 3 pages -->
    <q-btn-group class="q-mb-lg">
      <q-btn to="/" label="Home" no-caps :color="$route.path === '/' ? 'primary' : 'grey-4'" />
      <q-btn to="/about" label="About" no-caps :color="$route.path === '/about' ? 'primary' : 'grey-4'" />
      <q-btn to="/contact" label="Contact" no-caps :color="$route.path === '/contact' ? 'primary' : 'grey-4'" />
    </q-btn-group>

    <!-- Transition wraps router-view with out-in mode:
         old page leaves completely before new page enters -->
    <Transition name="slide-fade" mode="out-in">
      <router-view />
    </Transition>
  </q-page>
</template>

<script setup>
// The transition is applied around <router-view> so each page
// animates as the route changes. mode="out-in" ensures the
// outgoing page finishes its leave animation before the incoming
// page starts its enter animation, preventing overlap.
</script>

<style scoped>
/* Slide-fade enter: slide in from the right with fade */
.slide-fade-enter-active {
  transition: all 0.3s ease;
}
.slide-fade-leave-active {
  transition: all 0.3s ease;
}
.slide-fade-enter-from {
  transform: translateX(20px);
  opacity: 0;
}
.slide-fade-leave-to {
  transform: translateX(-20px);
  opacity: 0;
}
</style>
