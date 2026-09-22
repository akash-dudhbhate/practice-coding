/**
 * LESSON 07 — Pinia State Management
 * MEDIUM P02 — Two Stores in One File
 * ============================================
 * CONCEPT: State is modular — each domain gets its own store. A component
 * can pull from as many stores as it needs; each use*Store() call returns
 * the same shared instance.
 *
 * PROBLEM: Export `useUserStore` (id 'user': `user` ref, `login(userData)`,
 * `logout`) and `useProductStore` (id 'product': `products` ref,
 * `fetchProducts` async action filling a mock list). Include a component
 * (template in a comment or object) that uses both — user info + product
 * list loaded on mount.
 *
 * TRY THIS: export const useUserStore = defineStore('user', () => {...});
 * export const useProductStore = defineStore('product', () => {...});
 * In setup: const { user } = storeToRefs(userStore); onMounted(fetchProducts)
 *
 * EXPECTED OUTPUT: A login/logout area plus a "Load Products" flow rendering
 * the mock products.
 *
 * CHECK: python3 check.py medium/p02
 */
// TODO: write your stores here
