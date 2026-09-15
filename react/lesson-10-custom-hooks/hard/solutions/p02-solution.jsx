// Lesson 10 — Hard P02: useForm
import { useState, useCallback } from "react";
function useForm(initialValues, validate) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const handleChange = useCallback((e) => {
    const { name, value } = e.target;
    setValues((v) => ({ ...v, [name]: value }));
    setErrors((prev) => ({ ...prev, [name]: "" }));
  }, []);
  const handleSubmit = useCallback((onSubmit) => (e) => {
    e.preventDefault();
    const errs = validate ? validate(values) : {};
    setErrors(errs);
    if (Object.keys(errs).length === 0) onSubmit(values);
  }, [values, validate]);
  return { values, errors, handleChange, handleSubmit };
}
function RegistrationForm() {
  const { values, errors, handleChange, handleSubmit } = useForm(
    { name: "", email: "", password: "", confirm: "" },
    (v) => {
      const e = {};
      if (!v.name) e.name = "Required";
      if (!v.email.includes("@")) e.email = "Invalid email";
      if (v.password.length < 8) e.password = "Min 8 chars";
      if (v.password !== v.confirm) e.confirm = "Mismatch";
      return e;
    }
  );
  return (
    <form onSubmit={handleSubmit((v) => alert("Registered: " + v.name))}>
      <input name="name" value={values.name} onChange={handleChange} placeholder="Name" />
      {errors.name && <span style={{ color: "red" }}> {errors.name}</span>}<br />
      <input name="email" value={values.email} onChange={handleChange} placeholder="Email" />
      {errors.email && <span style={{ color: "red" }}> {errors.email}</span>}<br />
      <input name="password" type="password" value={values.password} onChange={handleChange} placeholder="Password" />
      {errors.password && <span style={{ color: "red" }}> {errors.password}</span>}<br />
      <input name="confirm" type="password" value={values.confirm} onChange={handleChange} placeholder="Confirm" />
      {errors.confirm && <span style={{ color: "red" }}> {errors.confirm}</span>}<br />
      <button type="submit">Register</button>
    </form>
  );
}
export default RegistrationForm;
