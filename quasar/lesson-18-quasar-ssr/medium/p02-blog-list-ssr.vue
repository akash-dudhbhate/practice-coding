<!--
LESSON 18 — Quasar SSR
MEDIUM P02 — Blog List with preFetch + SEO
============================================
CONCEPT: preFetch fills the store before render so list pages arrive
pre-populated. Exporting title/meta (or calling useMeta/useHead) gives
each page unique SEO tags.

PROBLEM: A blog index: preFetch fetches all posts (simulated Promise) into
the store; the template renders a q-list of items linking to /posts/:id
with title + excerpt; export page-unique title and meta
(description + og:title + og:description).

TRY THIS: const preFetch = async ({ store }) => { store.posts = await fetchPosts() }
const meta = { description: '...', 'og:title': '...' }
export { preFetch, title, meta }

EXPECTED OUTPUT: The server-rendered list contains all post links and the
unique meta tags appear in the head.

CHECK: python3 check.py medium/p02
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
