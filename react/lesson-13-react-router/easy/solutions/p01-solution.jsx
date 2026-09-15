// Lesson 13 — Easy P01: 3 routes with 404
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
function Home() { return <h1>Home</h1>; }
function About() { return <h1>About</h1>; }
function Contact() { return <h1>Contact</h1>; }
function NotFound() { return <h1>404 - Page Not Found</h1>; }
function App() {
  return (
    <BrowserRouter>
      <nav><Link to="/">Home</Link> | <Link to="/about">About</Link> | <Link to="/contact">Contact</Link></nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
