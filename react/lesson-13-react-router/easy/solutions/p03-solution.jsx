// Lesson 13 — Easy P03: Dynamic route with useParams
import { BrowserRouter, Routes, Route, Link, useParams } from "react-router-dom";
function UserProfile() {
  const { username } = useParams();
  return <h1>Profile: {username}</h1>;
}
function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/user/alice">Alice</Link> | <Link to="/user/bob">Bob</Link> | <Link to="/user/charlie">Charlie</Link>
      </nav>
      <Routes>
        <Route path="/user/:username" element={<UserProfile />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
