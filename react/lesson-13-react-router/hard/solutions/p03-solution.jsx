// Lesson 13 — Hard P03: E-commerce routing structure
import { BrowserRouter, Routes, Route, Link, Outlet, useParams } from "react-router-dom";
function Home() { return <h1>Home</h1>; }
function Products() { return <div><h1>Products</h1><Link to="/products/1">Product 1</Link></div>; }
function ProductDetail() { const { id } = useParams(); return <h1>Product {id}</h1>; }
function Cart() { return <h1>Cart</h1>; }
function Checkout() { return <h1>Checkout</h1>; }
function AccountLayout() { return <div><aside><Link to="/account">Orders</Link> | <Link to="/account/settings">Settings</Link></aside><main><Outlet /></main></div>; }
function Orders() { return <h2>Orders</h2>; }
function Settings() { return <h2>Settings</h2>; }
function App() {
  return (
    <BrowserRouter>
      <nav><Link to="/">Home</Link> | <Link to="/products">Products</Link> | <Link to="/cart">Cart</Link> | <Link to="/account">Account</Link></nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/products" element={<Products />} />
        <Route path="/products/:id" element={<ProductDetail />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/checkout" element={<Checkout />} />
        <Route path="/account" element={<AccountLayout />}>
          <Route index element={<Orders />} />
          <Route path="settings" element={<Settings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
export default App;
