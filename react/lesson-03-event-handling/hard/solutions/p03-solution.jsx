// Lesson 03 — Hard P03: Keyboard-Navigable Dropdown
import { useState } from "react";
function KeyboardDropdown() {
  const items = ["Option 1", "Option 2", "Option 3"];
  const [open, setOpen] = useState(false);
  const [selected, setSelected] = useState(0);
  const handleKeyDown = (e) => {
    if (e.key === "Enter") setOpen(!open);
    else if (e.key === "ArrowDown" && open) setSelected((s) => Math.min(s + 1, items.length - 1));
    else if (e.key === "ArrowUp" && open) setSelected((s) => Math.max(s - 1, 0));
    else if (e.key === "Escape") setOpen(false);
  };
  return (
    <div tabIndex={0} onKeyDown={handleKeyDown} style={{ outline: "1px solid #333", padding: "8px", cursor: "pointer" }}>
      {items[selected]} ▼
      {open && (
        <ul style={{ listStyle: "none", padding: 0, margin: "8px 0", border: "1px solid #ddd" }}>
          {items.map((item, i) => (
            <li key={i} style={{ padding: "4px 8px", background: i === selected ? "#667eea" : "#fff", color: i === selected ? "#fff" : "#000" }} onClick={() => { setSelected(i); setOpen(false); }}>{item}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
export default KeyboardDropdown;
