<!--
  Lesson 13 - Hard - P01: Animated Accordion FAQ
  5 questions, click to expand/collapse using q-slide-transition.
  Only one open at a time. Rotation animation on expand/collapse icon.
-->
<template>
  <q-page class="q-pa-md">
    <div class="text-h5 q-mb-md">FAQ Accordion</div>

    <q-list bordered separator>
      <q-expansion-item
        v-for="(faq, index) in faqs"
        :key="index"
        v-model="faq.expanded"
        :label="faq.question"
        :header-class="faq.expanded ? 'bg-blue-1' : ''"
        expand-icon="expand_more"
        @update:model-value="closeOthers(index)"
      >
        <q-card-section class="text-body2 text-grey-8">
          {{ faq.answer }}
        </q-card-section>
      </q-expansion-item>
    </q-list>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

// FAQ data with expanded state tracking
const faqs = ref([
  {
    question: 'What is Quasar Framework?',
    answer: 'Quasar is a Vue.js based framework for building cross-platform apps — SPA, PWA, SSR, mobile, and desktop — from a single codebase.',
    expanded: false,
  },
  {
    question: 'How do I install Quasar?',
    answer: 'Run `npm i -g @quasar/cli` then `quasar create my-app`. Navigate to the project and run `quasar dev` to start the dev server.',
    expanded: false,
  },
  {
    question: 'Can I use Quasar with Vite?',
    answer: 'Yes, Quasar supports Vite as a build tool. Use `quasar create` and select Vite when prompted during project creation.',
    expanded: false,
  },
  {
    question: 'Does Quasar support dark mode?',
    answer: 'Yes, Quasar has built-in dark mode support. Use $q.dark.toggle() or $q.dark.set(true/false) to control it programmatically.',
    expanded: false,
  },
  {
    question: 'How do I deploy a Quasar PWA?',
    answer: 'Run `quasar build -m pwa` to generate the PWA build in dist/pwa. Deploy the contents to any static hosting service like Netlify, Vercel, or GitHub Pages.',
    expanded: false,
  },
])

// Close all other FAQs when one opens (accordion behavior)
function closeOthers(currentIndex) {
  faqs.value.forEach((faq, i) => {
    if (i !== currentIndex) {
      faq.expanded = false
    }
  })
}
</script>

<style scoped>
/* q-expansion-item handles the slide transition and icon rotation internally.
   We add a subtle background highlight when expanded via header-class. */
</style>
