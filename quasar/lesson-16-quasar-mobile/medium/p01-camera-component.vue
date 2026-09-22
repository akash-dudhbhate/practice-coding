<!--
LESSON 16 — Quasar Mobile (Capacitor)
MEDIUM P01 — Camera Component with Web Fallback
============================================
CONCEPT: Gate native plugins behind $q.platform.is.capacitor and import
them dynamically (await import('@capacitor/camera')) so web builds don't
break. On the web, a hidden <input type="file" accept="image/*"> + FileReader
is your fallback.

PROBLEM: A Take Photo button: on Capacitor call Camera.getPhoto
(quality, resultType DataUrl, source Prompt, saveToGallery) and show the
result in q-img; on web click a hidden file input and read it as data URL.
Handle permission denial/cancel with a friendly $q.notify. Include a Clear
button.

TRY THIS: if (!$q.platform.is.capacitor) { fileInput.value?.click(); return }
const { Camera, CameraResultType, CameraSource } = await import('@capacitor/camera')

EXPECTED OUTPUT: Mobile opens the camera sheet; web opens a file picker —
either way the photo previews and errors toast politely.

CHECK: python3 check.py medium/p01
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
