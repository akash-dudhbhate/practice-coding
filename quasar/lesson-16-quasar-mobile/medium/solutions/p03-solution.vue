<!--
  Share Component (Capacitor Share)
  ---------------------------------
  - Button to share text and a URL using the Capacitor Share plugin
  - Falls back to the Web Share API (navigator.share) on supported browsers
  - Final fallback: copy the text to the clipboard
  - Shows a Quasar notification on success or failure
-->
<template>
  <q-page class="column flex-center q-pa-md">
    <div class="text-h6 q-mb-md">Share This App</div>

    <q-card flat bordered class="q-pa-md q-mb-md text-center" style="max-width: 360px">
      <p class="text-body1">{{ shareText }}</p>
      <p class="text-primary text-weight-medium">{{ shareUrl }}</p>
    </q-card>

    <q-btn
      color="primary"
      icon="share"
      label="Share"
      :loading="sharing"
      @click="share"
    />

    <q-btn
      v-if="!$q.platform.is.capacitor"
      flat
      color="grey-7"
      icon="content_copy"
      label="Copy Link"
      class="q-mt-sm"
      @click="copyToClipboard"
    />
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'

const $q = useQuasar()

// Content to share — in a real app these could come from props or route
const shareText = ref('Check out this awesome Quasar app!')
const shareUrl = ref('https://example.com')
const sharing = ref(false)

/**
 * Attempt to share via Capacitor → Web Share API → clipboard copy.
 */
async function share() {
  sharing.value = true

  const fullText = `${shareText.value} ${shareUrl.value}`

  try {
    // 1. Capacitor Share plugin (mobile)
    if ($q.platform.is.capacitor) {
      const { Share } = await import('@capacitor/share')
      await Share.share({
        title: 'Quasar App',
        text: shareText.value,
        url: shareUrl.value,
        dialogTitle: 'Share via',
      })
      $q.notify({ type: 'positive', message: 'Shared successfully' })
      return
    }

    // 2. Web Share API (supported on most modern mobile browsers)
    if (navigator.share) {
      await navigator.share({
        title: 'Quasar App',
        text: shareText.value,
        url: shareUrl.value,
      })
      $q.notify({ type: 'positive', message: 'Shared successfully' })
      return
    }

    // 3. Clipboard fallback
    await copyToClipboard()
  } catch (err) {
    // User cancelled the share sheet — not a real error
    if (err?.message?.includes('cancel') || err?.name === 'AbortError') {
      return
    }
    $q.notify({ type: 'negative', message: 'Sharing failed' })
  } finally {
    sharing.value = false
  }
}

/**
 * Copy the share text + URL to the clipboard and notify.
 */
async function copyToClipboard() {
  const fullText = `${shareText.value} ${shareUrl.value}`

  try {
    if (navigator.clipboard) {
      await navigator.clipboard.writeText(fullText)
    } else {
      // Legacy fallback using a temporary textarea
      const textarea = document.createElement('textarea')
      textarea.value = fullText
      document.body.appendChild(textarea)
      textarea.select()
      document.execCommand('copy')
      document.body.removeChild(textarea)
    }
    $q.notify({ type: 'positive', message: 'Link copied to clipboard' })
  } catch {
    $q.notify({ type: 'negative', message: 'Failed to copy link' })
  }
}
</script>

<style scoped>
.q-page {
  gap: 8px;
}
</style>
