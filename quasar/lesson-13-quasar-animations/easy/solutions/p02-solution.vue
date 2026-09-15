<!--
  Lesson 13 - Easy - P02: Expandable Section
  Uses q-slide-transition to slide content in/out.
  Button toggles between "Expand" and "Collapse". Uses v-show.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">Slide Transition</div>

    <q-btn
      color="primary"
      :icon="expanded ? 'expand_less' : 'expand_more'"
      :label="expanded ? 'Collapse' : 'Expand'"
      no-caps
      class="q-mb-md"
      @click="expanded = !expanded"
    />

    <!-- q-slide-transition provides smooth height animation -->
    <q-slide-transition>
      <div v-show="expanded" class="expand-content">
        <div class="text-body1">
          This section slides in and out smoothly using Quasar's
          q-slide-transition component. It animates the height of the
          container, making it perfect for expandable/collapsible sections.
        </div>
        <p class="q-mt-md">
          You can put any content here — text, images, forms, or other
          Quasar components. The transition handles the height animation
          automatically.
        </p>
      </div>
    </q-slide-transition>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const expanded = ref(false)
</script>

<style scoped>
.expand-content {
  padding: 20px;
  background: #f5f5f5;
  border-radius: 8px;
  overflow: hidden;
}
</style>
