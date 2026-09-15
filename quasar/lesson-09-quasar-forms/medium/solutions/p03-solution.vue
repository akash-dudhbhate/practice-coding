<template>
  <!-- File upload form using QFile - multiple images with previews -->
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg">
      <q-card-section>
        <div class="text-h5">Image Upload</div>
      </q-card-section>
      <q-card-section>
        <q-form @submit="onSubmit" class="q-gutter-md">
          <!-- QFile for multiple image uploads -->
          <q-file
            v-model="files"
            label="Upload Images (JPG, PNG - max 5MB each)"
            multiple
            accept=".jpg,.jpeg,.png,image/jpeg,image/png"
            max-file-size="5242880"
            @rejected="onRejected"
            outlined
          >
            <template #prepend>
              <q-icon name="attach_file" />
            </template>
          </q-file>

          <!-- File previews -->
          <div v-if="previewFiles.length" class="row q-col-gutter-md q-mt-sm">
            <div v-for="(preview, index) in previewFiles" :key="index" class="col-4 col-sm-3 col-md-2">
              <q-img :src="preview.url" :ratio="1" spinner-color="primary">
                <div class="absolute-bottom text-caption text-center">
                  {{ preview.name }}
                </div>
              </q-img>
            </div>
          </div>

          <q-btn type="submit" label="Upload" color="primary" :disable="!files.length" />
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const files = ref([])
const previewFiles = ref([])

// Watch files and generate previews
watch(files, (newFiles) => {
  // Clear old previews
  previewFiles.value.forEach((p) => URL.revokeObjectURL(p.url))
  previewFiles.value = []

  // Generate new previews for valid image files
  newFiles.forEach((file) => {
    if (file.type.startsWith('image/')) {
      previewFiles.value.push({
        name: file.name,
        url: URL.createObjectURL(file),
      })
    }
  })
}, { deep: true })

// Notify when files are rejected (wrong type or too large)
function onRejected(rejectedEntries) {
  rejectedEntries.forEach((entry) => {
    $q.notify({
      type: 'negative',
      message: `File "${entry.file.name}" rejected: ${entry.failedPropValidation}`,
      timeout: 5000,
    })
  })
}

function onSubmit() {
  $q.notify({
    type: 'positive',
    message: `${files.value.length} file(s) uploaded successfully!`,
  })
}
</script>

<style scoped>
.q-card {
  max-width: 600px;
  margin: 0 auto;
}
</style>
