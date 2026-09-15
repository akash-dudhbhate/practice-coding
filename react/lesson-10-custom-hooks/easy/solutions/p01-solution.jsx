// Lesson 10 — Easy P01: useToggle
import { useState, useCallback } from "react";
function useToggle(initial = false) {
  const [value, setValue] = useState(initial);
  const toggle = useCallback(() => setValue((v) => !v), []);
  const setTrue = useCallback(() => setValue(true), []);
  const setFalse = useCallback(() => setValue(false), []);
  return { value, toggle, setTrue, setFalse };
}
function ToggleDemo() {
  const { value, toggle } = useToggle(false);
  return (
    <div>
      <button onClick={toggle}>{value ? "Hide" : "Show"}</button>
      {value && <p>Toggle content visible!</p>}
    </div>
  );
}
export default ToggleDemo;
