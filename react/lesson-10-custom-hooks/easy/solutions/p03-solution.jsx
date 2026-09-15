// Lesson 10 — Easy P03: useWindowSize
import { useState, useEffect } from "react";
function useWindowSize() {
  const [size, setSize] = useState({ width: window.innerWidth, height: window.innerHeight });
  useEffect(() => {
    const onResize = () => setSize({ width: window.innerWidth, height: window.innerHeight });
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, []);
  return size;
}
function WindowDemo() {
  const { width, height } = useWindowSize();
  return <p>Window: {width} x {height}</p>;
}
export default WindowDemo;
