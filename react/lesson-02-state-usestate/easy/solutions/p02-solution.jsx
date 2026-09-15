// Lesson 02 — Easy P02: Toggle Text
import { useState } from "react";
function Toggle() {
  const [isOn, setIsOn] = useState(false);
  return <button onClick={() => setIsOn(!isOn)}>{isOn ? "ON" : "OFF"}</button>;
}
export default Toggle;
