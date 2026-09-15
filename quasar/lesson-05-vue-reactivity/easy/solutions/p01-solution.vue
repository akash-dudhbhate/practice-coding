<template>
  <div class="q-pa-md">
    <p>Title: {{ title }}</p>
    <p>Author: {{ book.author }}</p>
    <p>Year: {{ book.year }}</p>
    <q-btn label="Update All" color="primary" @click="updateAll" class="q-mt-sm" />
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const title = ref('Vue 3 Guide')
const book = reactive({ author: 'Evan You', year: 2020 })

function updateAll() {
  title.value = 'Updated Title'
  book.author = 'New Author'
  book.year = 2024
}
</script>
