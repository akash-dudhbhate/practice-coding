/*
LESSON 17 — Zustand
HARD P03 — Complete E-Commerce Store (Store-Only)
============================================
CONCEPT: This capstone is the full middleware stack: `create(devtools(persist(...)))` — devtools wires Redux DevTools for time-travel debugging, persist + partialize keeps only `cart` and `wishlist` across reloads.
PROBLEM: Build `useEcommerceStore = create(devtools(persist((set, get) => ({...}), {name:"ecommerce", partialize: (s) => ({cart: s.cart, wishlist: s.wishlist})})))`. State: `products`, `cart`, `wishlist`, `notifications`, `user`. Actions: `setProducts`, `addToCart` (merge by id, qty++), `removeFromCart`, `toggleWishlist` (id in/out), `addNotification`, `removeNotification`, `login`, `logout`. Export the hook — no components needed this time.
TRY THIS: In a console/DevTools: call `useEcommerceStore.getState().addToCart({id:1, price:5})`, inspect state, reload — cart persists.
EXPECTED OUTPUT: All actions mutate correctly; Redux DevTools shows each action; cart+wishlist persist.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
