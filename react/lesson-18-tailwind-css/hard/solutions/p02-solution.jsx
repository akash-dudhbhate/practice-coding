// Lesson 18 — Hard P02: Dark mode toggle
import { useState, useEffect } from "react";
function DarkModeApp() {
  const [dark, setDark] = useState(() => localStorage.getItem("theme") === "dark");
  useEffect(() => {
    document.documentElement.classList.toggle("dark", dark);
    localStorage.setItem("theme", dark ? "dark" : "light");
  }, [dark]);
  return (
    <div className="p-8 bg-white dark:bg-gray-900 min-h-screen transition-colors">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">Dark Mode Demo</h1>
      <p className="text-gray-600 dark:text-gray-300 mb-4">Toggle between light and dark themes.</p>
      <button onClick={() => setDark(!dark)} className="px-4 py-2 rounded bg-blue-500 text-white hover:bg-blue-600 dark:bg-blue-600 dark:hover:bg-blue-700">
        {dark ? "☀️ Light" : "🌙 Dark"}
      </button>
      <div className="mt-8 grid grid-cols-3 gap-4">
        {[1, 2, 3].map((n) => <div key={n} className="p-6 rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white">Card {n}</div>)}
      </div>
    </div>
  );
}
export default DarkModeApp;
