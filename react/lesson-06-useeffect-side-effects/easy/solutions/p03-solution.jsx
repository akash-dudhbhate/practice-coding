// Lesson 06 — Easy P03: Window Width Tracker
import { useState, useEffect } from "react";
function WindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);
  useEffect(() => {
    const onResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, []);
  return <p>Window width: {width}px</p>;
}
export default WindowWidth;
