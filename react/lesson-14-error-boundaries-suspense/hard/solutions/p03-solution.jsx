// Lesson 14 — Hard P03: Code-split app with per-route Suspense + ErrorBoundary
import { lazy, Suspense, Component } from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
class ErrorBoundary extends Component {
  constructor(props) { super(props); this.state = { hasError: false }; }
  static getDerivedStateFromError() { return { hasError: true }; }
  reset = () => this.setState({ hasError: false }); 
  render() {
    if (this.state.hasError) return <div><p>Failed to load. <button onClick={this.reset}>Retry</button></p></div>;
    return this.props.children;
  }
}
const Home = lazy(() => import("./Home"));
const About = lazy(() => import("./About"));
const Products = lazy(() => import("./Products"));
const Contact = lazy(() => import("./Contact"));
const Admin = lazy(() => import("./Admin"));
function App() {
  return (
    <BrowserRouter>
      <nav><Link to="/">Home</Link> | <Link to="/about">About</Link> | <Link to="/products">Products</Link> | <Link to="/contact">Contact</Link> | <Link to="/admin">Admin</Link></nav>
      <Routes>
        <Route path="/" element={<ErrorBoundary><Suspense fallback={<div className="skeleton">Loading...</div>}><Home /></Suspense></ErrorBoundary>} />
        <Route path="/about" element={<ErrorBoundary><Suspense fallback={<div className="skeleton">Loading...</div>}><About /></Suspense></ErrorBoundary>} />
        <Route path="/products" element={<ErrorBoundary><Suspense fallback={<div className="skeleton">Loading...</div>}><Products /></Suspense></ErrorBoundary>} />
        <Route path="/contact" element={<ErrorBoundary><Suspense fallback={<div className="skeleton">Loading...</div>}><Contact /></Suspense></ErrorBoundary>} />
        <Route path="/admin" element={<ErrorBoundary><Suspense fallback={<div className="skeleton">Loading...</div>}><Admin /></Suspense></ErrorBoundary>} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
