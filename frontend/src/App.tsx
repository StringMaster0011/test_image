import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import AdminPage from "./pages/AdminPage";
import UserPage from "./pages/UserPage";

const App: React.FC = () => {
  return (
    <Router>
      <nav style={{ marginBottom: "1rem" }}>
        <Link to="/admin" style={{ marginRight: "1rem" }}>Admin</Link>
        <Link to="/user">User</Link>
      </nav>
      <Routes>
        <Route path="/admin" element={<AdminPage />} />
        <Route path="/user" element={<UserPage />} />
      </Routes>
    </Router>
  );
};

export default App;
