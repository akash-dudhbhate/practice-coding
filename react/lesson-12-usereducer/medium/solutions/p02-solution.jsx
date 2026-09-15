// Lesson 12 — Medium P02: Multi-step form with useReducer
import { useReducer } from "react";
const reducer = (state, action) => {
  switch (action.type) {
    case "NEXT_STEP": return { ...state, step: state.step + 1 };
    case "PREV_STEP": return { ...state, step: Math.max(1, state.step - 1) };
    case "UPDATE_FIELD": return { ...state, formData: { ...state.formData, [action.field]: action.value } };
    case "SET_ERROR": return { ...state, errors: { ...state.errors, [action.field]: action.error } };
    default: return state;
  }
};
function MultiStepForm() {
  const [state, dispatch] = useReducer(reducer, { step: 1, formData: { name: "", email: "" }, errors: {} });
  return (
    <div>
      <p>Step: {state.step}</p>
      {state.step === 1 && <input placeholder="Name" value={state.formData.name} onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "name", value: e.target.value })} />}
      {state.step === 2 && <input placeholder="Email" value={state.formData.email} onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "email", value: e.target.value })} />}
      {state.step === 3 && <div><p>Name: {state.formData.name}</p><p>Email: {state.formData.email}</p></div>}
      <button onClick={() => dispatch({ type: "PREV_STEP" })}>Back</button>
      <button onClick={() => dispatch({ type: "NEXT_STEP" })}>Next</button>
    </div>
  );
}
export default MultiStepForm;
