<!--
  Lesson 01 - Quasar Basics - Hard - Problem 02
  q-color picker with live preview using q-card.
  Shows selected color and a preview box.
-->
<template>
  <q-page class="flex flex-center column q-gutter-md">
    <h2 class="text-h5">Color Picker</h2>

    <div class="row q-gutter-md">
      <!-- q-color lets the user pick a color; v-model holds the hex string -->
      <q-color v-model="selectedColor" />

      <!-- Preview card showing the selected color -->
      <q-card flat bordered style="min-width: 250px;">
        <q-card-section>
          <div class="text-subtitle2 text-grey-8">Selected Color</div>
          <div class="text-h6 text-weight-bold">{{ selectedColor }}</div>
        </q-card-section>

        <!-- The preview box background uses the selected color -->
        <q-card-section>
          <div
            class="preview-box"
            :style="{ backgroundColor: selectedColor }"
          ></div>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// Holds the hex color string, defaulting to a nice blue
const selectedColor = ref('#1976d2')
</script>

<style scoped>
.preview-box {
  width: 100%;
  height: 120px;
  border-radius: 8px;
  border: 1px solid #ccc;
  transition: background-color 0.2s ease;
}
</style>
