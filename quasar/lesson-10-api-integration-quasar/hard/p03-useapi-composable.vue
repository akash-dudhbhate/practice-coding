<!--
LESSON 10 — API Integration in Quasar
HARD P03 — useApi Fetching Composable
============================================
CONCEPT: A data-fetching composable takes an async function and returns
{ data, loading, error, refetch }. Calling refetch on mount, on window
focus, and via a button keeps data fresh with zero extra code.

PROBLEM: An inline `useApi(asyncFn)` composable: `data`/`loading`/`error`
refs, async `refetch()` wrapping the call in try/catch/finally, auto-fetch
in onMounted (and onActivated), a window 'focus' listener, and a component
using it to list fetched items with a manual Refetch button.

TRY THIS: function useApi(asyncFn) { ...; onMounted(refetch);
  window.addEventListener('focus', refetch); return { data, loading, error, refetch } }
const { data, loading, error, refetch } = useApi(async () => (await fetch(url)).json())

EXPECTED OUTPUT: The list loads on mount and on window focus; the Refetch
button re-pulls on demand with loading/error feedback.

CHECK: python3 check.py hard/p03
-->
<template>
  <!-- TODO: write your template here -->
</template>

<script setup>
// TODO: write your script here
</script>
