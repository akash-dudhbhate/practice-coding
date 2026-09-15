// Lesson 13 — Medium P01: Login redirect with useNavigate
import { BrowserRouter, Routes, Route, useNavigate } from "react-router-dom";
function Login() {
  const navigate = useNavigate();
  const handleSubmit = (e) => { e.preventDefault(); navigate("/dashboard"); };
  return <form onSubmit={handleSubmit}><button type="submit">Login</button></form>;
}
function Dashboard() {
  const navigate = useNavigate();
  return <div><h1>Dashboard</h1><button onClick={() => navigate(-1)}>Back</button></div>;
}
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
