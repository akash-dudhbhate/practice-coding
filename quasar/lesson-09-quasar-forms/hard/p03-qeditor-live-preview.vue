<!--
LESSON 09 — Quasar Forms
HARD P03 — QEditor + Live Preview
============================================
CONCEPT: q-editor is a rich text editor bound with v-model (HTML string).
Render it back with v-html — but sanitize first: strip <script> tags and
on* event attributes in a computed.

PROBLEM: A q-editor with a toolbar (bold/italic/underline, lists, link,
undo/redo) bound to `content`, a computed `sanitizedContent` that removes
scripts and inline handlers, a v-html live preview card, plus Save (stores
+ notifies) and Clear buttons.

TRY THIS: html.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
html.replace(/\son\w+="[^"]*"/gi, '')

EXPECTED OUTPUT: Typing in the editor renders live below; Save stores the
clean HTML and shows a confirmation banner.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
