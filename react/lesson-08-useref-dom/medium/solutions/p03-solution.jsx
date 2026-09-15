// Lesson 08 — Medium P03: CustomInput with forwardRef
import { useRef, forwardRef } from "react";
const CustomInput = forwardRef((props, ref) => (
  <input ref={ref} {...props} style={{ border: "2px solid #667eea", padding: "8px", borderRadius: "4px" }} />
));
function Parent() {
  const inputRef = useRef(null);
  return (
    <div>
      <CustomInput ref={inputRef} placeholder="Custom input" />
      <button onClick={() => inputRef.current.focus()}>Focus Custom Input</button>
    </div>
  );
}
export default Parent;
