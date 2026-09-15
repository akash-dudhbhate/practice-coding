// Lesson 11 — Hard P01: Shopping Cart with Context + useReducer
import { createContext, useContext, useReducer } from "react";
const CartContext = createContext(null);
const cartReducer = (state, action) => {
  switch (action.type) {
    case "ADD_ITEM": {
      const existing = state.items.find((i) => i.id === action.item.id);
      if (existing) return { ...state, items: state.items.map((i) => i.id === action.item.id ? { ...i, qty: i.qty + 1 } : i) };
      return { ...state, items: [...state.items, { ...action.item, qty: 1 }] };
    }
    case "REMOVE_ITEM": return { ...state, items: state.items.filter((i) => i.id !== action.id) };
    case "UPDATE_QTY": return { ...state, items: state.items.map((i) => i.id === action.id ? { ...i, qty: action.qty } : i) };
    case "CLEAR": return { items: [], total: 0 };
    default: return state;
  }
};
export function CartProvider({ children }) {
  const [state, dispatch] = useReducer(cartReducer, { items: [], total: 0 });
  const total = state.items.reduce((sum, i) => sum + i.price * i.qty, 0);
  return <CartContext.Provider value={{ ...state, total, dispatch }}>{children}</CartContext.Provider>;
}
export function useCart() { const ctx = useContext(CartContext); if (!ctx) throw new Error("useCart must be used within CartProvider"); return ctx; }
