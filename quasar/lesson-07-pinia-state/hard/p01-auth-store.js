/**
 * LESSON 07 — Pinia State Management
 * HARD P01 — Complete Auth Store
 * ============================================
 * CONCEPT: Real auth stores hold user + token, expose an isAuthenticated
 * getter, wrap an async login in try/catch/finally (loading + error state),
 * and persist both to localStorage.
 *
 * PROBLEM: Export `useAuthStore` (id 'auth') with `user`, `token`, `loading`,
 * `error` refs, `isAuthenticated` computed, async `login(credentials)`
 * (mock with setTimeout + Promise, persist on success, set error on
 * failure), and `logout` clearing everything. Include a login-form
 * component (template in a comment or object) using the store.
 *
 * TRY THIS: const isAuthenticated = computed(() => !!token.value);
 * async function login(c) { loading.value = true; try { await api...; persist() } catch(e) { error.value = e.message } finally { loading.value = false } }
 *
 * EXPECTED OUTPUT: A store driving a login form: spinner while "logging in",
 * error message on bad credentials, state restored after refresh.
 *
 * CHECK: python3 check.py hard/p01
 */
// TODO: write your store here
