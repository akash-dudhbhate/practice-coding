// Lesson 19 — Hard P03: Test ShoppingCart with Context
import { render, screen, fireEvent } from "@testing-library/react";
import { CartProvider, useCart } from "../CartContext";

const TestComponent = () => {
  const { items, addItem, removeItem, updateQty, total, count } = useCart();
  return (
    <div>
      <button onClick={() => addItem({ id: 1, name: "Apple", price: 1 })}>Add Apple</button>
      <button onClick={() => addItem({ id: 2, name: "Banana", price: 0.5 })}>Add Banana</button>
      <button onClick={() => removeItem(1)}>Remove Apple</button>
      <button onClick={() => updateQty(1, 3)}>Update Qty</button>
      <span data-testid="count">{count}</span>
      <span data-testid="total">{total.toFixed(2)}</span>
      {items.length === 0 && <span>Cart is empty</span>}
      {items.map((i) => <div key={i.id}>{i.name} x{i.qty}</div>)}
    </div>
  );
};

const renderApp = () => render(<CartProvider><TestComponent /></CartProvider>);

test("starts empty", () => {
  renderApp();
  expect(screen.getByText("Cart is empty")).toBeInTheDocument();
});

test("adds items", () => {
  renderApp();
  fireEvent.click(screen.getByText("Add Apple"));
  fireEvent.click(screen.getByText("Add Banana"));
  expect(screen.getByText(/Apple x1/)).toBeInTheDocument();
  expect(screen.getByText(/Banana x1/)).toBeInTheDocument();
  expect(screen.getByTestId("count").textContent).toBe("2");
});

test("removes items", () => {
  renderApp();
  fireEvent.click(screen.getByText("Add Apple"));
  fireEvent.click(screen.getByText("Remove Apple"));
  expect(screen.getByText("Cart is empty")).toBeInTheDocument();
});

test("updates quantity", () => {
  renderApp();
  fireEvent.click(screen.getByText("Add Apple"));
  fireEvent.click(screen.getByText("Update Qty"));
  expect(screen.getByText(/Apple x3/)).toBeInTheDocument();
});

test("calculates total", () => {
  renderApp();
  fireEvent.click(screen.getByText("Add Apple"));
  fireEvent.click(screen.getByText("Add Banana"));
  expect(screen.getByTestId("total").textContent).toBe("1.50");
});
