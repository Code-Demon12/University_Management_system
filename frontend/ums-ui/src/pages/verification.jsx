import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function OtpVerify(){
  const [otp,setOtp] = useState("");
  const [error,setError] = useState("");
  const navigate = useNavigate();

  const verifyOtp = async () => {
    if(otp.length !== 6){
      setError("Enter valid 6-digit OTP");
      return;
    }

    setError("");

    // 🔐 TEMP SIMULATION (will come from backend later)
    // Example response from backend:
    /*
    {
      token: "jwt-token",
      role: "admin",
      branch: "CSE"
    }
    */

    const fakeBackendResponse = {
      token: "demo-token",
      role: "admin" // change this to test roles
      // roles: student | faculty | staff | admin | super-admin
    };

    localStorage.setItem("token", fakeBackendResponse.token);
    localStorage.setItem("user", JSON.stringify({ role: fakeBackendResponse.role }));

    // 🎯 Role-based redirect
    if(fakeBackendResponse.role === "student") navigate("/student");
    else if(fakeBackendResponse.role === "faculty") navigate("/faculty");
    else if(fakeBackendResponse.role === "staff") navigate("/staff");
    else if(fakeBackendResponse.role === "admin") navigate("/admin");
    else if(fakeBackendResponse.role === "super-admin") navigate("/super-admin");
    else navigate("/login");
  };

  return(
    <div style={{
      minHeight:"100vh",
      display:"flex",
      alignItems:"center",
      justifyContent:"center",
      background:"#020617"
    }}>
      <div style={{
        background:"#fff",
        padding:"30px",
        borderRadius:"12px",
        width:"350px",
        boxShadow:"0 0 20px rgba(0,0,0,0.2)"
      }}>
        <h2>Email Verification</h2>

        <input
          placeholder="Enter OTP"
          value={otp}
          onChange={e=>setOtp(e.target.value)}
          style={{width:"100%",margin:"10px 0",padding:"10px"}}
        />

        {error && <p style={{color:"red"}}>{error}</p>}

        <button onClick={verifyOtp}
          style={{width:"100%",padding:"10px",marginTop:"10px"}}
        >
          Verify OTP
        </button>
      </div>
    </div>
  );
}
