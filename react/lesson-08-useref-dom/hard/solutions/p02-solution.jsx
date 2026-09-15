// Lesson 08 — Hard P02: ScrollToTop Button
import { useState, useEffect } from "react";
function ScrollToTop() {
  const [visible, setVisible] = useState(false);
  useEffect(() => {
    const onScroll = () => setVisible(window.scrollY > 200);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);
  return visible ? (
    <button onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })} style={{ position: "fixed", bottom: 20, right: 20 }}>
      ↑ Top
    </button>
  ) : null;
}
export default ScrollToTop;
