<template>
  <div class="q-pa-md">
    <q-linear-progress v-if="loading" indeterminate color="primary" />
    <q-banner v-if="error" class="bg-negative text-white">
      {{ error }}
      <template #action>
        <q-btn flat label="Back to Shop" to="/shop" />
      </template>
    </q-banner>

    <div v-if="product && !loading">
      <h4>{{ product.name }}</h4>
      <p class="text-h5 text-primary">{{ product.price }}</p>
      <p>{{ product.description }}</p>

      <!-- Reviews -->
      <h6>Reviews ({{ reviews.length }})</h6>
      <q-list bordered>
        <q-item v-for="review in reviews" :key="review.id">
          <q-item-section>
            <q-item-label>{{ review.author }} — {{ review.rating }}/5</q-item-label>
            <q-item-label caption>{{ review.comment }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>

      <!-- Related products -->
      <h6>Related Products</h6>
      <div class="row q-gutter-md">
        <q-card v-for="related in relatedProducts" :key="related.id" class="col-4" :to="`/shop/${related.id}`">
          <q-card-section>{{ related.name }}</q-card-section>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const product = ref(null)
const reviews = ref([])
const relatedProducts = ref([])
const loading = ref(false)
const error = ref(null)

// Rich SEO meta tags (title, description, OG, Twitter, product schema)
const seoMeta = {
  title: product.value ? `${product.value.name} — Shop` : 'Product',
  meta: {
    description: product.value?.description || 'Product page',
    'og:title': product.value?.name || 'Product',
    'og:description': product.value?.description || '',
    'og:type': 'product',
    'og:image': product.value?.image || '',
    'twitter:card': 'summary_large_image',
    'twitter:title': product.value?.name || 'Product',
    'twitter:description': product.value?.description || '',
  },
  // Structured data for Google (JSON-LD)
  script: {
    type: 'application/ld+json',
    innerHTML: JSON.stringify({
      '@context': 'https://schema.org/',
      '@type': 'Product',
      name: product.value?.name,
      description: product.value?.description,
      offers: {
        '@type': 'Offer',
        price: product.value?.price,
        priceCurrency: 'USD',
      },
      aggregateRating: {
        '@type': 'AggregateRating',
        ratingValue: '4.5',
        reviewCount: String(reviews.value.length),
      },
    }),
  },
}

// preFetch: fetch product, reviews, and related products in parallel
const preFetch = async ({ store, currentRoute, redirect }) => {
  const productId = currentRoute.params.id
  const fetchProduct = (id) => new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id === 'missing') reject(new Error('Product not found'))
      else resolve({ id, name: `Product ${id}`, price: '$99.99', description: 'Great product', image: '/img.jpg' })
    }, 100)
  })
  const fetchReviews = (id) => new Promise((resolve) => {
    setTimeout(() => resolve([
      { id: 1, author: 'Alice', rating: 5, comment: 'Excellent!' },
      { id: 2, author: 'Bob', rating: 4, comment: 'Good value' },
    ]), 100)
  })
  const fetchRelated = (id) => new Promise((resolve) => {
    setTimeout(() => resolve([
      { id: parseInt(id) + 1, name: 'Related Product 1' },
      { id: parseInt(id) + 2, name: 'Related Product 2' },
    ]), 100)
  })

  try {
    const [p, rev, related] = await Promise.all([
      fetchProduct(productId),
      fetchReviews(productId),
      fetchRelated(productId),
    ])
    store.product = p
    store.reviews = rev
    store.relatedProducts = related
  } catch (e) {
    redirect('/404')
  }
}

export { preFetch, seoMeta }
</script>
