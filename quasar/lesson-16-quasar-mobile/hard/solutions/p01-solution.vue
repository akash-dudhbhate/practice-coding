<!--
  Mobile Photo Gallery
  --------------------
  - Take photos using the Capacitor Camera plugin (web file-input fallback)
  - Display captured photos in a responsive grid
  - Swipe left/right to navigate between photos in a fullscreen viewer
  - Long-press a photo to delete it (with confirmation)
  - Share an individual photo via Capacitor Share / Web Share API
  - Shows an empty state when no photos have been captured
-->
<template>
  <q-page class="q-pa-md">
    <!-- Header -->
    <div class="row items-center justify-between q-mb-md">
      <div class="text-h6">Photo Gallery ({{ photos.length }})</div>
      <q-btn
        color="primary"
        icon="add_a_photo"
        label="Take Photo"
        :loading="taking"
        @click="takePhoto"
      />
    </div>

    <!-- Empty state -->
    <div
      v-if="photos.length === 0"
      class="column flex-center text-grey-5"
      style="min-height: 300px"
    >
      <q-icon name="photo_library" size="72px" />
      <p class="q-mt-md">No photos yet. Tap "Take Photo" to get started.</p>
    </div>

    <!-- Photo grid -->
    <div v-else class="row q-col-gutter-sm">
      <div
        v-for="(photo, index) in photos"
        :key="photo.id"
        class="col-4 col-sm-3"
      >
        <q-img
          :src="photo.dataUrl"
          ratio="1"
          class="cursor-pointer gallery-thumb"
          @click="openViewer(index)"
          v-touch-hold="() => confirmDelete(photo.id)"
        >
          <!-- Overlay with action buttons on hover/tap -->
          <div class="absolute-bottom row justify-end q-pa-xs">
            <q-btn
              flat
              dense
              round
              color="white"
              icon="share"
              @click.stop="sharePhoto(photo)"
            />
            <q-btn
              flat
              dense
              round
              color="white"
              icon="delete"
              @click.stop="confirmDelete(photo.id)"
            />
          </div>
        </q-img>
      </div>
    </div>

    <!-- Fullscreen viewer dialog -->
    <q-dialog v-model="viewerOpen" full-width full-height>
      <q-card class="column no-wrap">
        <q-bar class="bg-black text-white">
          <div>Photo {{ viewerIndex + 1 }} of {{ photos.length }}</div>
          <q-space />
          <q-btn dense flat icon="close" v-close-popup />
        </q-bar>

        <q-card-section
          class="col flex-center bg-black"
          v-touch-swipe.left="nextPhoto"
          v-touch-swipe.right="prevPhoto"
        >
          <q-img
            v-if="currentPhoto"
            :src="currentPhoto.dataUrl"
            fit="contain"
            style="max-height: 70vh"
          />
        </q-card-section>

        <q-card-actions align="center" class="bg-black text-white">
          <q-btn flat icon="chevron_left" :disable="viewerIndex === 0" @click="prevPhoto" />
          <q-btn flat icon="share" label="Share" @click="sharePhoto(currentPhoto)" />
          <q-btn
            flat
            icon="chevron_right"
            :disable="viewerIndex === photos.length - 1"
            @click="nextPhoto"
          />
        </q-card-actions>
      </q-card>
    </q-dialog>

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
import { ref, computed } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// ---- State ---------------------------------------------------------------
const photos = ref([]) // [{ id, dataUrl }]
const taking = ref(false)
const fileInput = ref(null)
const viewerOpen = ref(false)
const viewerIndex = ref(0)

// Currently viewed photo (computed from index)
const currentPhoto = computed(() => photos.value[viewerIndex.value] || null)

// ---- Photo capture -------------------------------------------------------
async function takePhoto() {
  if (!$q.platform.is.capacitor) {
    fileInput.value?.click()
    return
  }
  try {
    taking.value = true
    const { Camera, CameraResultType, CameraSource } = await import('@capacitor/camera')
    const photo = await Camera.getPhoto({
      quality: 80,
      resultType: CameraResultType.DataUrl,
      source: CameraSource.Prompt,
      saveToGallery: true,
    })
    addPhoto(photo.dataUrl)
  } catch (err) {
    if (!err?.message?.includes('cancel')) {
      $q.notify({ type: 'negative', message: 'Camera error' })
    }
  } finally {
    taking.value = false
  }
}

function onFileSelected(event) {
  const file = event.target.files?.[0]
  if (!file) return
  const reader = new FileReader()
  reader.onload = (e) => addPhoto(e.target.result)
  reader.readAsDataURL(file)
  event.target.value = ''
}

function addPhoto(dataUrl) {
  photos.value.push({ id: Date.now(), dataUrl })
}

// ---- Viewer navigation ---------------------------------------------------
function openViewer(index) {
  viewerIndex.value = index
  viewerOpen.value = true
}

function nextPhoto() {
  if (viewerIndex.value < photos.value.length - 1) viewerIndex.value++
}

function prevPhoto() {
  if (viewerIndex.value > 0) viewerIndex.value--
}

// ---- Delete --------------------------------------------------------------
function confirmDelete(id) {
  $q.dialog({
    title: 'Delete Photo',
    message: 'Remove this photo from the gallery?',
    cancel: true,
    persistent: true,
  }).onOk(() => {
    photos.value = photos.value.filter((p) => p.id !== id)
    if (viewerOpen.value && currentPhoto.value === null) viewerOpen.value = false
    $q.notify({ type: 'info', message: 'Photo deleted' })
  })
}

// ---- Share ---------------------------------------------------------------
async function sharePhoto(photo) {
  if (!photo) return
  const text = 'Check out this photo from my Quasar app!'

  try {
    if ($q.platform.is.capacitor) {
      const { Share } = await import('@capacitor/share')
      await Share.share({ text })
    } else if (navigator.share) {
      await navigator.share({ text })
    } else {
      await navigator.clipboard.writeText(text)
    }
    $q.notify({ type: 'positive', message: 'Shared!' })
  } catch {
    $q.notify({ type: 'negative', message: 'Share cancelled or failed' })
  }
}
</script>

<style scoped>
.gallery-thumb {
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.15s;
}
.gallery-thumb:active {
  transform: scale(0.95);
}
</style>
