<!--
LESSON 10 — API Integration in Quasar
MEDIUM P03 — q-infinite-scroll List
============================================
CONCEPT: q-infinite-scroll calls @load(index, done) as you near the bottom —
done() ends that round, done(true) stops it forever. Push each new page into
a growing array; an empty page means the end.

PROBLEM: An infinite list fetching posts 10 at a time (?_page=&_limit=10),
appending to `items`, showing a spinner via the #loading slot, and a "No
more items" banner when the API returns an empty page (or on error).

TRY THIS: async function onLoad(index, doneFn) {
  const data = await fetch(`${API}?_page=${page.value}&_limit=10`).then(r => r.json());
  if (!data.length) { done.value = true; return doneFn() }
  items.value.push(...data); page.value++; doneFn() }

EXPECTED OUTPUT: Scrolling keeps appending 10 posts with a spinner; at the
end a "No more items to load" banner appears.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
