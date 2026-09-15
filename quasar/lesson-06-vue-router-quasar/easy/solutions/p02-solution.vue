<template>
  <!-- Navigation menu with 3 q-item components using `to` prop -->
  <q-list class="q-pa-md">
    <q-item
      v-for="link in navLinks"
      :key="link.to"
      :to="link.to"
      clickable
      exact
      active-class="text-primary bg-blue-1"
    >
      <q-item-section avatar>
        <q-icon :name="link.icon" />
      </q-item-section>
      <q-item-section>{{ link.label }}</q-item-section>
    </q-item>
  </q-list>
</template>

<script setup>
// Navigation links with route paths and icons
const navLinks = [
  { to: '/', label: 'Home', icon: 'home' },
  { to: '/about', label: 'About', icon: 'info' },
  { to: '/contact', label: 'Contact', icon: 'mail' },
]
</script>

<style scoped>
.q-list {
  max-width: 250px;
}
</style>
