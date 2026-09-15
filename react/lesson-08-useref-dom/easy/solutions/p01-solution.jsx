// Lesson 08 — Easy P01: Auto-focus input on mount
import { useRef, useEffect } from "react";
function AutoFocus() {
  const inputRef = useRef(null);
  useEffect(() => { inputRef.current.focus(); }, []);
  return <input ref={inputRef} type="text" placeholder="Auto-focused" />;
}
export default AutoFocus;
