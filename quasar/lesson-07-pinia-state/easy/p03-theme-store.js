/**
 * LESSON 07 — Pinia State Management
 * EASY P03 — Theme Store with $q.dark
 * ============================================
 * CONCEPT: Stores can drive app-wide UI state like dark mode. Quasar's
 * $q.dark.set(true/false) applies it globally; the store just holds and
 * toggles the boolean.
 *
 * PROBLEM: Export `useThemeStore` (id 'theme') with a `dark` ref(false) and a
 * `toggle` action (plus `setDark` optional). Include (in a comment or a
 * component) usage with $q.dark.set(dark.value).
 *
 * TRY THIS: const dark = ref(false); function toggle() { dark.value = !dark.value }
 * In component: const $q = useQuasar(); $q.dark.set(dark.value)
 *
 * EXPECTED OUTPUT: A toggleable dark-mode store; applying it flips Quasar
 * into dark theme.
 *
 * CHECK: python3 check.py easy/p03
 */
// TODO: write your store here
