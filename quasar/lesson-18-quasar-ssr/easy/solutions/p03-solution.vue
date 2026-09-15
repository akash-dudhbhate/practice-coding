<!--
  SEO Meta Tags Component
  -----------------------
  Sets page-level SEO metadata using Quasar's useHead composable
  (powered by @vueuse/head / Unhead).  This works during SSR so the
  tags are present in the initial server-rendered HTML — verify by
  viewing the page source.

  Tags set:
  - <title>
  - <meta name="description">
  - Open Graph: og:title, og:description, og:image, og:url
  - Twitter Card: twitter:card, twitter:title, twitter:description
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h4 q-mb-md">SEO Meta Tags Demo</div>

    <q-card flat bordered class="q-pa-lg">
      <p class="text-body1">
        This page sets SEO meta tags that appear in the server-rendered
        HTML.  Open the page source (Ctrl+U) to verify the following
        tags are present:
      </p>
      <ul>
        <li><code>&lt;title&gt;</code> — page title</li>
        <li><code>&lt;meta name="description"&gt;</code> — page summary</li>
        <li><code>&lt;meta property="og:*"&gt;</code> — Open Graph tags</li>
        <li><code>&lt;meta name="twitter:*"&gt;</code> — Twitter Card tags</li>
      </ul>
    </q-card>
  </q-page>
</template>

<script setup>
import { useHead } from '@vueuse/head'

// Static SEO content — in a real app this would come from route params
// or a CMS / API call during preFetch.
const pageTitle = 'Quasar SSR SEO Demo'
const pageDescription =
  'A demonstration of server-side rendered SEO meta tags in a Quasar app, including Open Graph and Twitter Card tags.'
const pageImage = 'https://example.com/og-image.png'
const pageUrl = 'https://example.com/seo-demo'

// useHead sets the tags during SSR (in the initial HTML) and updates
// them on the client during navigation.
useHead({
  // <title>
  title: pageTitle,

  // <meta> tags
  meta: [
    { name: 'description', content: pageDescription },

    // Open Graph — used by Facebook, LinkedIn, etc.
    { property: 'og:title', content: pageTitle },
    { property: 'og:description', content: pageDescription },
    { property: 'og:image', content: pageImage },
    { property: 'og:url', content: pageUrl },
    { property: 'og:type', content: 'website' },

    // Twitter Card
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: pageTitle },
    { name: 'twitter:description', content: pageDescription },
    { name: 'twitter:image', content: pageImage },
  ],

  // <link> tags (canonical URL)
  link: [
    { rel: 'canonical', href: pageUrl },
  ],
})
</script>

<style scoped>
code {
  background: rgba(0, 0, 0, 0.08);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.9em;
}
</style>
