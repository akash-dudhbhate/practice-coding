// Lesson 13 — Hard P02: Multi-step wizard with location state
import { BrowserRouter, Routes, Route, useNavigate, useLocation, Link } from "react-router-dom";
function Step1() {
  const navigate = useNavigate();
  const location = useLocation();
  return <div><h2>Step 1: Name</h2><input placeholder="Name" defaultValue={location.state?.name || ""} onBlur={(e) => navigate("/wizard/step2", { state: { ...location.state, name: e.target.value } })} /><Link to="/wizard/step2">Next</Link></div>;
}
function Step2() {
  const navigate = useNavigate();
  const location = useLocation();
  if (!location.state?.name) return <div><p>Complete step 1 first</p><Link to="/wizard/step1">Go to Step 1</Link></div>;
  return <div><h2>Step 2: Email</h2><input placeholder="Email" defaultValue={location.state?.email || ""} onBlur={(e) => navigate("/wizard/step3", { state: { ...location.state, email: e.target.value } })} /><Link to="/wizard/step1">Back</Link> | <Link to="/wizard/step3">Next</Link></div>;
}
function Step3() {
  const location = useLocation();
  if (!location.state?.email) return <div><p>Complete step 2 first</p><Link to="/wizard/step2">Go to Step 2</Link></div>;
  return <div><h2>Step 3: Review</h2><p>Name: {location.state.name}</p><p>Email: {location.state.email}</p></div>;
}
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/wizard/step1" element={<Step1 />} />
        <Route path="/wizard/step2" element={<Step2 />} />
        <Route path="/wizard/step3" element={<Step3 />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
