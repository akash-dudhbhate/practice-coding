<!--
  Lesson 13 - Hard - P03: Complete Loading Experience
  Skeleton loading (2s), content fades in, loading bar at top,
  success notification after load. GPU-accelerated animations.
-->
<template>
  <q-page class="q-pa-md">
    <!-- Top loading bar — visible during loading -->
    <q-linear-progress
      v-if="loading"
      indeterminate
      color="primary"
      class="loading-bar"
      reverse
    />

    <div class="text-h5 q-mb-md">Complete Loading Experience</div>

    <!-- Skeleton state during loading -->
    <Transition name="fade">
      <div v-if="loading" class="content-area">
        <div class="row q-col-gutter-md">
          <div class="col-12 col-md-6" v-for="i in 4" :key="`skel-${i}`">
            <q-card flat bordered>
              <q-skeleton height="150px" square animation="wave" />
              <q-card-section>
                <q-skeleton type="text" width="50%" height="20px" class="q-mb-sm" animation="wave" />
                <q-skeleton type="text" animation="wave" />
                <q-skeleton type="text" width="80%" animation="wave" />
              </q-card-section>
            </q-card>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Actual content — fades in after loading -->
    <Transition name="fade">
      <div v-if="!loading" class="content-area">
        <div class="row q-col-gutter-md">
          <div class="col-12 col-md-6" v-for="item in items" :key="item.id">
            <q-card flat bordered class="content-card">
              <q-img :src="item.image" height="150px" />
              <q-card-section>
                <div class="text-h6">{{ item.title }}</div>
                <p class="text-body2 text-grey-7">{{ item.description }}</p>
              </q-card-section>
            </q-card>
          </div>
        </div>
      </div>
    </Transition>

    <!-- Reload button to replay the loading experience -->
    <q-btn
      color="primary"
      icon="refresh"
      label="Reload"
      no-caps
      class="q-mt-md"
      @click="reload"
    />
  </q-page>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()
const loading = ref(true)

// Sample content items
const items = ref([
  { id: 1, title: 'Mountain View', description: 'Breathtaking mountain landscapes.', image: 'https://cdn.quasar.dev/img/parallax1.jpg' },
  { id: 2, title: 'City Lights', description: 'Urban nightlife at its finest.', image: 'https://cdn.quasar.dev/img/parallax2.jpg' },
  { id: 3, title: 'Ocean Waves', description: 'Relaxing seaside scenery.', image: 'https://cdn.quasar.dev/img/parallax1.jpg' },
  { id: 4, title: 'Forest Trail', description: 'Peaceful nature walks.', image: 'https://cdn.quasar.dev/img/parallax2.jpg' },
])

// Simulate loading with 2-second delay, then show success notification
function loadData() {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    $q.notify({
      type: 'positive',
      message: 'Content loaded successfully!',
      icon: 'check_circle',
      timeout: 3000,
    })
  }, 2000)
}

// Reload handler
function reload() {
  loadData()
}

// Initial load on mount
onMounted(() => {
  loadData()
})
</script>

<style scoped>
/* GPU-accelerated fade transition using transform and opacity */
.loading-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 9999;
}

.content-area {
  will-change: opacity, transform; /* Hint to browser for GPU acceleration */
}

/* Fade transition for content swap */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s ease, transform 0.4s ease;
  will-change: opacity, transform;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.content-card {
  transition: transform 0.2s ease;
}
.content-card:hover {
  transform: translateY(-4px);
}
</style>
