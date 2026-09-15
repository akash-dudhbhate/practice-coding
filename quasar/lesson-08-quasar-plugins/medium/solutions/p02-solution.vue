<template>
  <!-- Responsive grid using $q.screen -->
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Responsive Grid</div>
    <div class="text-subtitle1 q-mb-md">
      Current breakpoint: <q-badge color="primary">{{ currentBreakpoint }}</q-badge>
    </div>
    <div class="row q-col-gutter-md">
      <div
        v-for="n in 9"
        :key="n"
        class="col-12 col-sm-6 col-md-4"
      >
        <q-card>
          <q-card-section>
            <div class="text-h6">Card {{ n }}</div>
            <div class="text-subtitle2">Grid item</div>
          </q-card-section>
          <q-card-section>
            This card adapts to the screen size.
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { computed } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Display current breakpoint from $q.screen
// xs = 1 column, sm = 2 columns, md+ = 3 columns (handled by col classes)
const currentBreakpoint = computed(() => {
  if ($q.screen.xs) return 'xs (1 column)'
  if ($q.screen.sm) return 'sm (2 columns)'
  return 'md+ (3 columns)'
})
</script>

<style scoped>
.q-page {
  max-width: 900px;
  margin: 0 auto;
}
</style>
