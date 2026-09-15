<!--
  SSR-Aware Component
  -------------------
  Demonstrates how to write a component that behaves correctly on both
  the server and the client:

  - process.env.SERVER is true during SSR (Node) rendering
  - process.env.CLIENT is true in the browser
  - window / document are ONLY accessed inside onMounted() (they do
    not exist on the server)
  - The rendered HTML differs based on environment so you can verify
    server vs. client output in the page source.
-->
<template>
  <q-page class="column flex-center q-pa-md">
    <div class="text-h4 q-mb-md">SSR Environment Detector</div>

    <!-- Server-rendered message (present in initial HTML) -->
    <q-banner
      class="q-mb-md"
      :class="isServer ? 'bg-blue-2 text-blue-9' : 'bg-green-2 text-green-9'"
    >
      <template #avatar>
        <q-icon :name="isServer ? 'dns' : 'computer'" />
      </template>
      This component was rendered on the
      <b>{{ isServer ? 'SERVER' : 'CLIENT' }}</b>.
    </q-banner>

    <!-- Client-only information (hydrated after mount) -->
    <q-card v-if="clientInfo" flat bordered class="q-pa-md">
      <div class="text-subtitle1 q-mb-sm">Client-only data (available after mount):</div>
      <div>Viewport: {{ clientInfo.viewport }}</div>
      <div>User Agent: {{ clientInfo.userAgent }}</div>
      <div>Platform: {{ clientInfo.platform }}</div>
    </q-card>

    <q-spinner v-else color="primary" size="32px" class="q-mt-md" />
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// Detect the rendering environment at module-evaluation time.
// Quasar injects process.env.SERVER and process.env.CLIENT booleans.
const isServer = ref(process.env.SERVER)
const isClient = ref(process.env.CLIENT)

// Client-only data — populated in onMounted (never on the server)
const clientInfo = ref(null)

onMounted(() => {
  // Safe to access window here — onMounted only runs in the browser
  clientInfo.value = {
    viewport: `${window.innerWidth}×${window.innerHeight}`,
    userAgent: window.navigator.userAgent,
    platform: window.navigator.platform,
  }

  // Log to the browser console for verification
  console.log('[SSR Detector] Hydrated on client. Server flag was:', isServer.value)
})

// On the server, log to stdout (no console object in the browser pre-hydration)
if (process.env.SERVER) {
  console.log('[SSR Detector] Rendering on server')
}
</script>

<style scoped>
.q-banner {
  max-width: 500px;
  width: 100%;
}
</style>
