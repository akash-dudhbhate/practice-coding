// Lesson 17 — Medium P02: Cart store with computed total
import { create } from "zustand";
const useCartStore = create((set, get) => ({
  items: [],
  addItem: (item) => set((s) => {
    const existing = s.items.find((i) => i.id === item.id);
    if (existing) return { items: s.items.map((i) => i.id === item.id ? { ...i, qty: i.qty + 1 } : i) };
    return { items: [...s.items, { ...item, qty: 1 }] };
  }),
  removeItem: (id) => set((s) => ({ items: s.items.filter((i) => i.id !== id) })),
  updateQuantity: (id, qty) => set((s) => ({ items: s.items.map((i) => i.id === id ? { ...i, qty } : i) })),
  clearCart: () => set({ items: [] }),
  get total() { return get().items.reduce((sum, i) => sum + i.price * i.qty, 0); },
}));
function Cart() {
  const { items, addItem, removeItem, total } = useCartStore();
  return (
    <div>
      <button onClick={() => addItem({ id: 1, name: "Apple", price: 1 })}>Add Apple</button>
      <ul>{items.map((i) => <li key={i.id}>{i.name} x{i.qty} = ${i.price * i.qty} <button onClick={() => removeItem(i.id)}>Remove</button></li>)}</ul>
      <p>Total: ${total.toFixed(2)}</p>
    </div>
  );
}
export default Cart;
