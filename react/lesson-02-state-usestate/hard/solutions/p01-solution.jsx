// Lesson 02 — Hard P01: Shopping Cart
import { useState } from "react";
function ShoppingCart() {
  const products = [{ id: 1, name: "Apple", price: 1 }, { id: 2, name: "Banana", price: 0.5 }, { id: 3, name: "Cherry", price: 2 }];
  const [cart, setCart] = useState([]);
  const addToCart = (p) => setCart([...cart, { ...p, qty: 1 }]);
  const updateQty = (id, delta) => setCart(cart.map((item) => item.id === id ? { ...item, qty: Math.max(1, item.qty + delta) } : item));
  const removeFromCart = (id) => setCart(cart.filter((item) => item.id !== id));
  const total = cart.reduce((sum, item) => sum + item.price * item.qty, 0);
  return (
    <div>
      <h3>Products</h3>
      {products.map((p) => <button key={p.id} onClick={() => addToCart(p)}>Add {p.name}</button>)}
      <h3>Cart</h3>
      {cart.map((item) => (
        <div key={item.id}>
          {item.name} - ${item.price} x {item.qty}
          <button onClick={() => updateQty(item.id, 1)}>+</button>
          <button onClick={() => updateQty(item.id, -1)}>-</button>
          <button onClick={() => removeFromCart(item.id)}>Remove</button>
        </div>
      ))}
      <p>Total: ${total.toFixed(2)}</p>
    </div>
  );
}
export default ShoppingCart;
