<template>
  <!-- Detect platform using $q.platform -->
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Platform Information</div>
    <q-card class="q-pa-lg">
      <q-card-section>
        <q-list>
          <q-item>
            <q-item-section>Device Type</q-item-section>
            <q-item-section side>
              <q-badge :color="isMobile ? 'primary' : 'secondary'">
                {{ isMobile ? 'Mobile' : 'Desktop' }}
              </q-badge>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>OS</q-item-section>
            <q-item-section side>
              <q-badge color="info">
                {{ isIOS ? 'iOS' : isAndroid ? 'Android' : 'Other' }}
              </q-badge>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section>Browser</q-item-section>
            <q-item-section side>
              <q-badge color="accent">{{ browserName }}</q-badge>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { computed } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Platform detection using $q.platform
const isMobile = computed(() => $q.platform.is.mobile)
const isIOS = computed(() => $q.platform.is.ios)
const isAndroid = computed(() => $q.platform.is.android)
const browserName = computed(() => {
  const p = $q.platform
  if (p.is.chrome) return 'Chrome'
  if (p.is.firefox) return 'Firefox'
  if (p.is.safari) return 'Safari'
  if (p.is.edge) return 'Edge'
  if (p.is.opera) return 'Opera'
  return 'Unknown'
})
</script>

<style scoped>
.q-card {
  max-width: 450px;
  margin: 0 auto;
}
</style>
