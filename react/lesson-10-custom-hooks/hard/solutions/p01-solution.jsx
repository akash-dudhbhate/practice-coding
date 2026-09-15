// Lesson 10 — Hard P01: useEventListener
import { useEffect } from "react";
function useEventListener(eventName, handler, element = window) {
  useEffect(() => {
    element.addEventListener(eventName, handler);
    return () => element.removeEventListener(eventName, handler);
  }, [eventName, handler, element]);
}
function EventListenerDemo() {
  const [modalOpen, setModalOpen] = useState(true);
  useEventListener("keydown", (e) => { if (e.key === "Escape") setModalOpen(false); });
  useEventListener("scroll", () => console.log("Scroll:", window.scrollY));
  return (
    <div>
      {modalOpen && <div style={{ background: "#333", color: "#fff", padding: 20 }} onClick={() => setModalOpen(false)}>Press Escape or click to close</div>}
    </div>
  );
}
import { useState } from "react";
export default EventListenerDemo;
