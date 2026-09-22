/**
 * LESSON 07 — Pinia State Management
 * HARD P03 — Cross-Store Dependency (Cart needs Auth)
 * ============================================
 * CONCEPT: One store can use another — call useAuthStore() inside the cart
 * store's setup function. Then cart getters/actions can read auth state,
 * and a watcher can react to logout.
 *
 * PROBLEM: Export `useAuthStore` (user, token, isAuthenticated, login,
 * logout) and `useCartStore` that instantiates the auth store inside it.
 * Cart has: `visibleCart` computed ([] unless authenticated), `addItem`
 * that returns { success: false, reason: 'login_required' } when logged
 * out, and a watch on authStore.isAuthenticated that clears the cart on
 * logout.
 *
 * TRY THIS: const authStore = useAuthStore(); // inside cart store
 * const visibleCart = computed(() => authStore.isAuthenticated ? items.value : [])
 * watch(() => authStore.isAuthenticated, (ok) => { if (!ok) clearCart() })
 *
 * EXPECTED OUTPUT: Adding while logged out signals a login redirect; logging
 * out empties the cart automatically.
 *
 * CHECK: python3 check.py hard/p03
 */
// TODO: write your stores here
