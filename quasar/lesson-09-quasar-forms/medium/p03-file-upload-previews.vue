<!--
LESSON 09 — Quasar Forms
MEDIUM P03 — File Upload with Previews
============================================
CONCEPT: q-file picks files; `multiple`, `accept`, and `max-file-size`
constrain them, and @rejected catches violations. URL.createObjectURL(file)
makes a preview URL for q-img — revoke old URLs to avoid leaks.

PROBLEM: An image upload form: q-file with multiple + accept jpg/png +
max-file-size 5MB, @rejected notifying each rejection, a watch generating
q-img previews for image files, and an Upload submit button.

TRY THIS: <q-file v-model="files" multiple accept=".jpg,.jpeg,.png,image/*"
  max-file-size="5242880" @rejected="onRejected" />;
previewFiles.push({ name: file.name, url: URL.createObjectURL(file) })

EXPECTED OUTPUT: Picking images shows thumbnail previews; an oversized or
wrong-type file triggers a negative notification.

CHECK: python3 check.py medium/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
