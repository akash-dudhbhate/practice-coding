// Lesson 17 — Hard P03: Complete e-commerce store
import { create } from "zustand";
import { persist, devtools } from "zustand/middleware";
const useEcommerceStore = create(devtools(persist(
  (set, get) => ({
    products: [],
    cart: [],
    wishlist: [],
    notifications: [],
    user: null,
    setProducts: (products) => set({ products }),
    addToCart: (product) => set((s) => {
      const existing = s.cart.find((i) => i.id === product.id);
      if (existing) return { cart: s.cart.map((i) => i.id === product.id ? { ...i, qty: i.qty + 1 } : i) };
      return { cart: [...s.cart, { ...product, qty: 1 }] };
    }),
    removeFromCart: (id) => set((s) => ({ cart: s.cart.filter((i) => i.id !== id) })),
    toggleWishlist: (id) => set((s) => ({ wishlist: s.wishlist.includes(id) ? s.wishlist.filter((w) => w !== id) : [...s.wishlist, id] })),
    addNotification: (msg) => set((s) => ({ notifications: [...s.notifications, { id: Date.now(), msg }] })),
    removeNotification: (id) => set((s) => ({ notifications: s.notifications.filter((n) => n.id !== id) })),
    login: (user) => set({ user }),
    logout: () => set({ user: null }),
  }),
  { name: "ecommerce", partialize: (s) => ({ cart: s.cart, wishlist: s.wishlist }) }
)));
export default useEcommerceStore;
