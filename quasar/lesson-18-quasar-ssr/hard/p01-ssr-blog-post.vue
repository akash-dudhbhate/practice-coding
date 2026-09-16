<!--
LESSON 18 — Quasar SSR
HARD P01 — Complete SSR Blog Post Page
============================================
CONCEPT: A real SSR detail page: preFetch gets {store, currentRoute,
redirect}, fetches post + related posts in parallel, redirects to /404 on
missing data. Breadcrumbs, per-post SEO meta, loading + error states
complete the UX.

PROBLEM: A blog post page: q-breadcrumbs (Home → Blog → post title);
preFetch fetches the post and related posts via currentRoute.params.id
and redirect('/404')s on failure; renders title/date/content plus a
related-posts list linking to /blog/:id; export title/meta built from the
post; loading spinner and error banner states.

TRY THIS: const [p, related] = await Promise.all([fetchPost(id), fetchRelated(id)])
store.post = p; } catch { redirect('/404') }

EXPECTED OUTPUT: Server HTML has breadcrumbs, the post, related links and
SEO tags; a bad id 404s.

CHECK: python3 check.py hard/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
