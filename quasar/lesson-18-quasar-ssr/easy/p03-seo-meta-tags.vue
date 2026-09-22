<!--
LESSON 18 — Quasar SSR
EASY P03 — SEO Meta Tags (useHead)
============================================
CONCEPT: useHead (from @vueuse/head, or Quasar's useMeta) injects
title/meta/link tags during SSR so crawlers see them in the raw HTML —
not only after JS runs.

PROBLEM: Set the page title, a description meta, Open Graph tags
(og:title/description/image/url/type), Twitter Card tags
(twitter:card/title/description), and a canonical link. Show a card
explaining the tags were set.

TRY THIS: import { useHead } from '@vueuse/head'
useHead({ title: 'My Page', meta: [{ name: 'description', content: '...' },
  { property: 'og:title', content: '...' }], link: [{ rel: 'canonical', href: '...' }] })

EXPECTED OUTPUT: Ctrl+U page source contains the title and all meta tags.

CHECK: python3 check.py easy/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
