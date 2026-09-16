/**
 * LESSON 07 — Pinia State Management
 * MEDIUM P03 — Persistent User Store
 * ============================================
 * CONCEPT: Persist store state to localStorage: read it when the store is
 * created (initial ref value), write it inside a watch with { deep: true },
 * and remove the key when state goes null (logout).
 *
 * PROBLEM: Export `useUserStore` (id 'user') with `user` ref initialized
 * from localStorage key 'app_user' (JSON.parse), a watch that auto-saves
 * (or removes) on every change, and `login` / `logout` actions.
 *
 * TRY THIS: const user = ref(loadFromStorage());
 * watch(user, (u) => saveToStorage(u), { deep: true });
 * logout() just sets user.value = null — the watcher clears storage.
 *
 * EXPECTED OUTPUT: Login survives a simulated refresh (value read back from
 * localStorage); logout removes the stored key.
 *
 * CHECK: python3 check.py medium/p03
 */
// TODO: write your store here
