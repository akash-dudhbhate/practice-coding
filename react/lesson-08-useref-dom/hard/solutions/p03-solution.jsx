// Lesson 08 — Hard P03: CustomForm with forwardRef + useImperativeHandle
import { useRef, forwardRef, useImperativeHandle, useState } from "react";
const CustomForm = forwardRef((props, ref) => {
  const [value, setValue] = useState("");
  const inputRef = useRef(null);
  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
    clear: () => setValue(""),
    validate: () => value.length > 0,
    submit: () => { if (value.length > 0) alert("Submitted: " + value); },
  }));
  return <input ref={inputRef} value={value} onChange={(e) => setValue(e.target.value)} placeholder="Type something" />;
});
function Parent() {
  const formRef = useRef(null);
  return (
    <div>
      <CustomForm ref={formRef} />
      <button onClick={() => formRef.current.focus()}>Focus</button>
      <button onClick={() => formRef.current.clear()}>Clear</button>
      <button onClick={() => alert("Valid: " + formRef.current.validate())}>Validate</button>
      <button onClick={() => formRef.current.submit()}>Submit</button>
    </div>
  );
}
export default Parent;
