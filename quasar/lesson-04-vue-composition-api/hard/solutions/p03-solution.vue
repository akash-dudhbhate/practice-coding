<!--
  Lesson 04 - Vue Composition API - Hard - Problem 03
  Mouse position tracker: onMounted adds mousemove listener updating x/y refs.
  onUnmounted removes it. Display coordinates.
  Template ref to div, log width on mount.
-->
<template>
  <q-page class="q-pa-md">
    <h2 class="text-h6">Mouse Position Tracker</h2>

    <!-- Template ref attached to this div; we log its width on mount -->
    <div ref="boxRef" class="tracker-box">
      <p>Mouse X: <strong>{{ mouseX }}</strong></p>
      <p>Mouse Y: <strong>{{ mouseY }}</strong></p>
      <p class="text-caption text-grey-7">Move your mouse over the page to update coordinates.</p>
    </div>
  </q-page>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Mouse coordinates
const mouseX = ref(0)
const mouseY = ref(0)

// Template ref: bound to the div via ref="boxRef"
const boxRef = ref(null)

// The event handler must be a named function so we can remove it later
function handleMouseMove(event) {
  mouseX.value = event.clientX
  mouseY.value = event.clientY
}

// onMounted: add listener and log the div's width
onMounted(() => {
  window.addEventListener('mousemove', handleMouseMove)
  // Access the DOM element through the template ref's .value
  if (boxRef.value) {
    console.log('Tracker box width on mount:', boxRef.value.offsetWidth, 'px')
  }
})

// onUnmounted: remove listener to prevent memory leaks
onUnmounted(() => {
  window.removeEventListener('mousemove', handleMouseMove)
})
</script>

<style scoped>
.tracker-box {
  border: 2px dashed var(--q-primary, #1976d2);
  border-radius: 8px;
  padding: 24px;
  max-width: 400px;
}
</style>
