<!--
  Camera Component (Capacitor Camera)
  ------------------------------------
  - Button to take a photo using the Capacitor Camera plugin
  - Displays the captured photo
  - Saves the photo to the device gallery
  - Handles permission denial gracefully
  - Falls back to a standard <input type="file"> on the web platform
-->
<template>
  <q-page class="column flex-center q-pa-md">
    <div class="text-h6 q-mb-md">Take a Photo</div>

    <!-- Captured photo preview -->
    <q-img
      v-if="photoUrl"
      :src="photoUrl"
      spinner-color="primary"
      style="max-width: 320px; border-radius: 12px"
      class="q-mb-md shadow-2"
    />

    <!-- Placeholder when no photo yet -->
    <q-icon
      v-else
      name="photo_camera"
      size="80px"
      color="grey-5"
      class="q-mb-md"
    />

    <!-- Action buttons -->
    <div class="row q-gutter-md">
      <q-btn
        color="primary"
        icon="photo_camera"
        label="Take Photo"
        :loading="taking"
        @click="takePhoto"
      />
      <q-btn
        v-if="photoUrl"
        flat
        color="negative"
        icon="delete"
        label="Clear"
        @click="photoUrl = ''"
      />
    </div>

    <!-- Hidden web fallback input -->
    <input
      ref="fileInput"
      type="file"
      accept="image/*"
      capture="environment"
      style="display: none"
      @change="onFileSelected"
    />
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const photoUrl = ref('')
const taking = ref(false)
const fileInput = ref(null)

/**
 * Attempt to use the Capacitor Camera plugin.
 * If the plugin is unavailable (e.g. running in a plain browser),
 * fall back to the hidden <input type="file">.
 */
async function takePhoto() {
  // Web fallback — trigger the file input
  if (!$q.platform.is.capacitor) {
    fileInput.value?.click()
    return
  }

  try {
    taking.value = true
    // Dynamically import so the build does not fail on web-only projects
    const { Camera, CameraResultType, CameraSource } = await import('@capacitor/camera')

    const photo = await Camera.getPhoto({
      quality: 80,
      allowEditing: false,
      resultType: CameraResultType.DataUrl,
      source: CameraSource.Prompt, // let user pick camera or gallery
      saveToGallery: true,
    })

    photoUrl.value = photo.dataUrl || ''
  } catch (err) {
    // User denied camera permission or cancelled — show a friendly message
    handleCameraError(err)
  } finally {
    taking.value = false
  }
}

/**
 * Handle the file input change event (web fallback).
 */
function onFileSelected(event) {
  const file = event.target.files?.[0]
  if (!file) return

  const reader = new FileReader()
  reader.onload = (e) => {
    photoUrl.value = e.target.result
  }
  reader.readAsDataURL(file)

  // Reset so the same file can be selected again
  event.target.value = ''
}

/**
 * Show an appropriate notification based on the error type.
 */
function handleCameraError(err) {
  const msg =
    err?.message?.includes('permission')
      ? 'Camera permission denied. Please enable it in Settings.'
      : 'Unable to capture photo.'
  $q.notify({ type: 'negative', message: msg })
}
</script>

<style scoped>
.q-page {
  gap: 8px;
}
</style>
