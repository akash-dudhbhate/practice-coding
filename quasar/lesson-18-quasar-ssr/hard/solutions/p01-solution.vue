<template>
  <div class="q-pa-md">
    <!-- Breadcrumbs -->
    <q-breadcrumbs class="q-mb-md">
      <q-breadcrumbs-el label="Home" to="/" />
      <q-breadcrumbs-el label="Blog" to="/blog" />
      <q-breadcrumbs-el :label="post?.title || 'Loading...'" />
    </q-breadcrumbs>

    <!-- Loading state -->
    <q-linear-progress v-if="loading" indeterminate color="primary" />

    <!-- Error state (404) -->
    <q-banner v-if="error" class="bg-negative text-white">
      {{ error }}
      <template #action>
        <q-btn flat label="Back to Blog" to="/blog" />
      </template>
    </q-banner>

    <!-- Post detail -->
    <div v-if="post && !loading">
      <h4>{{ post.title }}</h4>
      <p class="text-grey">{{ post.date }}</p>
      <p>{{ post.content }}</p>

      <!-- Related posts -->
      <h6 class="q-mt-lg">Related Posts</h6>
      <q-list bordered>
        <q-item v-for="related in relatedPosts" :key="related.id" :to="`/blog/${related.id}`" clickable>
          <q-item-section>
            <q-item-label>{{ related.title }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const post = ref(null)
const relatedPosts = ref([])
const loading = ref(false)
const error = ref(null)

// SEO meta tags per post
const title = post.value ? `${post.value.title} — Blog` : 'Blog Post'
const meta = {
  description: post.value?.excerpt || 'Blog post',
}

// preFetch: fetch single post + related posts
const preFetch = async ({ store, currentRoute, redirect }) => {
  const postId = currentRoute.params.id
  const fetchPost = (id) => new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id === 'missing') reject(new Error('Post not found'))
      else resolve({ id, title: `Post ${id}`, date: '2024-01-15', content: 'Full content here...', excerpt: 'Excerpt...' })
    }, 100)
  })
  const fetchRelated = (id) => new Promise((resolve) => {
    setTimeout(() => resolve([
      { id: parseInt(id) + 1, title: 'Next Post' },
      { id: parseInt(id) + 2, title: 'Another Post' },
    ]), 100)
  })

  try {
    const [p, related] = await Promise.all([fetchPost(postId), fetchRelated(postId)])
    store.post = p
    store.relatedPosts = related
  } catch (e) {
    // 404 — redirect to 404 page
    redirect('/404')
  }
}

export { preFetch, title, meta }
</script>
