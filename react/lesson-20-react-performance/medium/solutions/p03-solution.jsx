// Lesson 20 — Medium P03: Route-level code splitting
import { lazy, Suspense, Component } from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
class ErrorBoundary extends Component {
  constructor(props) { super(props); this.state = { hasError: false }; }
  static getDerivedStateFromError() { return { hasError: true }; }
  render() { if (this.state.hasError) return <p>Failed to load route</p>; return this.props.children; }
}
// Code splitting: each route is a separate chunk
const Home = lazy(() => import("./Home"));
const About = lazy(() => import("./About"));
const Contact = lazy(() => import("./Contact"));
// Without code splitting, all 3 components would be in the initial bundle.
// With lazy(), each route loads its own chunk on demand, reducing initial bundle size.
function App() {
  return (
    <BrowserRouter>
      <nav><Link to="/">Home</Link> | <Link to="/about">About</Link> | <Link to="/contact">Contact</Link></nav>
      <ErrorBoundary>
        <Suspense fallback={<p>Loading route...</p>}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </Suspense>
      </ErrorBoundary>
    </BrowserRouter>
  );
}
export default App;
