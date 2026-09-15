<template>
  <div class="q-pa-md">
    <h4>Blog Posts</h4>
    <q-list bordered separator>
      <q-item v-for="post in posts" :key="post.id" :to="`/posts/${post.id}`" clickable>
        <q-item-section>
          <q-item-label>{{ post.title }}</q-item-label>
          <q-item-label caption>{{ post.excerpt }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// SEO meta tags — unique per page
const title = 'Blog Posts — My Blog'
const meta = {
  description: 'Browse all blog posts on My Blog',
  'og:title': 'Blog Posts — My Blog',
  'og:description': 'Browse all blog posts on My Blog',
}

// preFetch: fetch all posts on server and client
const preFetch = async ({ store }) => {
  // Simulate API call
  const fetchPosts = () => new Promise((resolve) => {
    setTimeout(() => {
      resolve([
        { id: 1, title: 'Getting Started with Quasar', excerpt: 'Learn the basics...' },
        { id: 2, title: 'SSR in Quasar', excerpt: 'Server-side rendering guide...' },
        { id: 3, title: 'PWA with Quasar', excerpt: 'Build installable apps...' },
      ])
    }, 100)
  })
  const posts = await fetchPosts()
  store.posts = posts
}

const posts = ref([])

// Read prefetched data (from Pinia or initial state)
if (typeof window !== 'undefined' && window.__INITIAL_STATE__?.posts) {
  posts.value = window.__INITIAL_STATE__.posts
}

export { preFetch, title, meta }
</script>
