<template>
  <div class="q-pa-md">
    <q-infinite-scroll @load="onLoad" :offset="250">
      <q-list bordered separator>
        <q-item v-for="item in items" :key="item.id">
          <q-item-section>
            <q-item-label>{{ item.title }}</q-item-label>
            <q-item-label caption>{{ item.body }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
      <template #loading>
        <div class="row justify-center q-my-md">
          <q-spinner color="primary" size="40px" />
        </div>
      </template>
    </q-infinite-scroll>
    <q-banner v-if="done" class="bg-grey-2 q-mt-md text-center">
      No more items to load.
    </q-banner>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const API = 'https://jsonplaceholder.typicode.com/posts'
const LIMIT = 10

const items = ref([])
const page = ref(1)
const done = ref(false)

async function onLoad(index, doneFn) {
  if (done.value) {
    doneFn()
    return
  }
  try {
    const res = await fetch(`${API}?_page=${page.value}&_limit=${LIMIT}`)
    const data = await res.json()
    if (data.length === 0) {
      done.value = true
      doneFn()
      return
    }
    items.value.push(...data)
    page.value++
    doneFn()
  } catch (e) {
    console.error(e)
    doneFn(true) // stop on error
  }
}
</script>
