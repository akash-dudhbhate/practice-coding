// Lesson 18 — Easy P03: Button with hover/focus/active states
function StyledButton() {
  return (
    <button className="bg-blue-500 text-white px-6 py-2 rounded transition-colors hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-400 active:scale-95">
      Click Me
    </button>
  );
}
export default StyledButton;
