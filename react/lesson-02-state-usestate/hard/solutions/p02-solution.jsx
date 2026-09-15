// Lesson 02 — Hard P02: Multi-Step Form
import { useState } from "react";
function MultiStepForm() {
  const [step, setStep] = useState(1);
  const [data, setData] = useState({ name: "", email: "" });
  const handleChange = (e) => setData({ ...data, [e.target.name]: e.target.value });
  const next = () => { if (step === 1 && !data.name) return; if (step === 2 && !data.email) return; setStep(step + 1); };
  const back = () => setStep(step - 1);
  return (
    <div>
      {step === 1 && <input name="name" value={data.name} onChange={handleChange} placeholder="Name" />}
      {step === 2 && <input name="email" value={data.email} onChange={handleChange} placeholder="Email" />}
      {step === 3 && (<div><h3>Review</h3><p>Name: {data.name}</p><p>Email: {data.email}</p></div>)}
      {step > 1 && <button onClick={back}>Back</button>}
      {step < 3 && <button onClick={next}>Next</button>}
      {step === 3 && <button onClick={() => alert("Submitted!")}>Submit</button>}
    </div>
  );
}
export default MultiStepForm;
