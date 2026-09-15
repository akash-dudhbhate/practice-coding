// Lesson 18 — Medium P02: Responsive navbar
import { useState } from "react";
function Navbar() {
  const [open, setOpen] = useState(false);
  return (
    <nav className="bg-white shadow p-4 flex justify-between items-center">
      <div className="text-xl font-bold">Logo</div>
      <div className="hidden md:flex gap-4">
        <a href="#" className="hover:text-blue-500">Home</a>
        <a href="#" className="hover:text-blue-500">About</a>
        <a href="#" className="hover:text-blue-500">Services</a>
        <a href="#" className="hover:text-blue-500">Contact</a>
      </div>
      <button className="md:hidden" onClick={() => setOpen(!open)}>☰</button>
      {open && (
        <div className="md:hidden absolute top-16 right-4 bg-white shadow-lg rounded p-4 flex flex-col gap-2">
          <a href="#" className="hover:text-blue-500">Home</a>
          <a href="#" className="hover:text-blue-500">About</a>
          <a href="#" className="hover:text-blue-500">Services</a>
          <a href="#" className="hover:text-blue-500">Contact</a>
        </div>
      )}
    </nav>
  );
}
export default Navbar;
