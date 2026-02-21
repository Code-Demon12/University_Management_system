//import logo from './logo.svg';
import './App.css';

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import OtpVerify from "./pages/verification";
import Admin from "./pages/Admin";
import SuperAdmin from "./pages/SuperAdmin";
import Student from "./pages/Student";
import Faculty from "./pages/Faculty";
import Analytics from "./pages/Analytics";
import Chatbot from "./pages/Chatbot";

import ProtectedRoute from "./components/ProtectedRoute";
import RoleGuard from "./components/RoleGuard";
import Layout from "./components/layouts/Layout";

export default function App(){
  return(
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login/>}/>
        {/* Public Routes */}
        <Route path="/login" element={<Login/>}/>
        <Route path="/otp-verify" element={<OtpVerify/>}/>

        {/* Protected Routes */}
        <Route element={<ProtectedRoute/>}>
          <Route element={<Layout/>}>

            <Route path="/student" element={<Student/>}/>
            <Route path="/faculty" element={<Faculty/>}/>
            <Route path="/chatbot" element={<Chatbot/>}/>

            {/* Admin */}
            <Route element={<RoleGuard role="admin"/>}>
              <Route path="/admin" element={<Admin/>}/>
              <Route path="/analytics" element={<Analytics/>}/>
            </Route>

            {/* Super Admin */}
            <Route element={<RoleGuard role="super-admin"/>}>
              <Route path="/super-admin" element={<SuperAdmin/>}/>
            </Route>

          </Route>
        </Route>

      </Routes>
    </BrowserRouter>
  );
}
