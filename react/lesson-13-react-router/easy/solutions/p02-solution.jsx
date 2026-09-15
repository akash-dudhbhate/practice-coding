// Lesson 13 — Easy P02: NavLink with active highlight
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
function Home() { return <h1>Home</h1>; }
function About() { return <h1>About</h1>; }
function Services() { return <h1>Services</h1>; }
function Contact() { return <h1>Contact</h1>; }
function App() {
  return (
    <BrowserRouter>
      <nav>
        <NavLink to="/" style={({ isActive }) => ({ color: isActive ? "red" : "blue" })}>Home</NavLink> | 
        <NavLink to="/about" style={({ isActive }) => ({ color: isActive ? "red" : "blue" })}>About</NavLink> |
        <NavLink to="/services" style={({ isActive }) => ({ color: isActive ? "red" : "blue" })}>Services</NavLink> |
        <NavLink to="/contact" style={({ isActive }) => ({ color: isActive ? "red" : "blue" })}>Contact</NavLink>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/services" element={<Services />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
