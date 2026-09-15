<!--
  Geolocation Component (Capacitor Geolocation)
  ----------------------------------------------
  - Button to request and display the device location
  - Shows latitude / longitude in a card
  - Provides a link to view the position on a map (OpenStreetMap iframe)
  - Handles permission denial and other errors with notifications
-->
<template>
  <q-page class="column flex-center q-pa-md">
    <div class="text-h6 q-mb-md">Your Location</div>

    <!-- Location data card -->
    <q-card v-if="location" flat bordered class="q-pa-md q-mb-md" style="min-width: 300px">
      <q-card-section>
        <div class="row justify-between">
          <span class="text-grey-7">Latitude</span>
          <span class="text-weight-medium">{{ location.latitude.toFixed(6) }}</span>
        </div>
        <div class="row justify-between">
          <span class="text-grey-7">Longitude</span>
          <span class="text-weight-medium">{{ location.longitude.toFixed(6) }}</span>
        </div>
        <div v-if="location.accuracy" class="row justify-between">
          <span class="text-grey-7">Accuracy</span>
          <span class="text-weight-medium">±{{ Math.round(location.accuracy) }} m</span>
        </div>
      </q-card-section>

      <!-- Map preview via OpenStreetMap embed -->
      <q-card-section class="q-pt-none">
        <iframe
          :src="mapUrl"
          width="100%"
          height="200"
          style="border: 0; border-radius: 8px"
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
        />
      </q-card-section>
    </q-card>

    <!-- Placeholder when no location yet -->
    <q-icon
      v-else
      name="location_on"
      size="64px"
      color="grey-5"
      class="q-mb-md"
    />

    <q-btn
      color="primary"
      icon="my_location"
      label="Get My Location"
      :loading="loading"
      @click="getLocation"
    />
  </q-page>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const location = ref(null)
const loading = ref(false)

// Build an OpenStreetMap embed URL from the current coordinates
const mapUrl = computed(() => {
  if (!location.value) return ''
  const { latitude, longitude } = location.value
  const bbox = `${longitude - 0.01},${latitude - 0.01},${longitude + 0.01},${latitude + 0.01}`
  return `https://www.openstreetmap.org/export/embed.html?bbox=${bbox}&layer=mapnik&marker=${latitude},${longitude}`
})

/**
 * Request the current device position.
 * Uses Capacitor Geolocation on mobile, falls back to the
 * browser navigator.geolocation API on the web.
 */
async function getLocation() {
  loading.value = true

  try {
    let coords

    if ($q.platform.is.capacitor) {
      // Capacitor plugin path
      const { Geolocation } = await import('@capacitor/geolocation')
      const perm = await Geolocation.checkPermissions()
      if (perm.location === 'denied') {
        const req = await Geolocation.requestPermissions()
        if (req.location === 'denied') {
          throw new Error('permission-denied')
        }
      }
      const result = await Geolocation.getCurrentPosition({ enableHighAccuracy: true })
      coords = result.coords
    } else {
      // Web fallback using the browser API
      coords = await getWebPosition()
    }

    location.value = coords
    $q.notify({ type: 'positive', message: 'Location retrieved' })
  } catch (err) {
    handleError(err)
  } finally {
    loading.value = false
  }
}

/**
 * Wrap the browser geolocation API in a Promise.
 */
function getWebPosition() {
  return new Promise((resolve, reject) => {
    if (!navigator.geolocation) {
      reject(new Error('unsupported'))
      return
    }
    navigator.geolocation.getCurrentPosition(
      (pos) => resolve(pos.coords),
      (err) => {
        if (err.code === err.PERMISSION_DENIED) {
          reject(new Error('permission-denied'))
        } else {
          reject(new Error('unavailable'))
        }
      },
      { enableHighAccuracy: true, timeout: 10000 }
    )
  })
}

/**
 * Map known error types to user-friendly messages.
 */
function handleError(err) {
  const messages = {
    'permission-denied': 'Location permission denied. Enable it in your settings.',
    unavailable: 'Location is currently unavailable. Try again later.',
    unsupported: 'Geolocation is not supported on this device.',
  }
  const msg = messages[err.message] || 'Unable to get location.'
  $q.notify({ type: 'negative', message: msg })
}
</script>

<style scoped>
.q-page {
  gap: 8px;
}
</style>
