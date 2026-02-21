import { Link } from "react-router-dom";
//import { LayoutDashboard, Users, Bot, BarChart3, Shield } from "lucide-react";

export default function Sidebar(){
  return(
    <div style={{
      width:"240px",
      background:"#020617",
      color:"#fff",
      padding:"20px"
    }}>
      <h2 style={{marginBottom:"30px"}}>UMS</h2>

      <nav style={{display:"flex",flexDirection:"column",gap:"15px"}}>
        <Link to="/student">Student</Link>
        <Link to="/faculty">Faculty</Link>
        <Link to="/admin">Admin</Link>
        <Link to="/analytics">Analytics</Link>
        <Link to="/chatbot">AI Chatbot</Link>
        <Link to="/super-admin">Super Admin</Link>
      </nav>
    </div>
  );
}
