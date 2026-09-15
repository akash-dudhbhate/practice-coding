// Lesson 12 — Medium P01: Shopping cart reducer
import { useReducer } from "react";
const reducer = (state, action) => {
  switch (action.type) {
    case "ADD_ITEM": {
      const existing = state.find((i) => i.id === action.item.id);
      if (existing) return state.map((i) => i.id === action.item.id ? { ...i, qty: i.qty + 1 } : i);
      return [...state, { ...action.item, qty: 1 }];
    }
    case "REMOVE_ITEM": return state.filter((i) => i.id !== action.id);
    case "UPDATE_QTY": return state.map((i) => i.id === action.id ? { ...i, qty: action.qty } : i);
    case "CLEAR": return [];
    default: return state;
  }
};
function Cart() {
  const [items, dispatch] = useReducer(reducer, []);
  const total = items.reduce((sum, i) => sum + i.price * i.qty, 0);
  return (
    <div>
      <button onClick={() => dispatch({ type: "ADD_ITEM", item: { id: 1, name: "Apple", price: 1 } })}>Add Apple</button>
      <ul>{items.map((i) => <li key={i.id}>{i.name} x{i.qty} = ${i.price * i.qty}</li>)}</ul>
      <p>Total: ${total}</p>
    </div>
  );
}
export default Cart;
