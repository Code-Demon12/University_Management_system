import { useState } from "react";

export default function Login(){
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");
  const [error,setError] = useState("");

  const handleLogin = () => {
    if(!email.endsWith("@bpai.in")){
      setError("Only university emails (@bpai.in) are allowed");
      return;
    }

    if(!email || !password){
      setError("All fields are required");
      return;
    }

    setError("");
    // 🔐 Backend auth call later
    console.log("Login allowed:", email);
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
        <h2 style={{textAlign:"center",marginBottom:"20px"}}>UMS Login</h2>

        <input
          placeholder="Email"
          value={email}
          onChange={e=>setEmail(e.target.value)}
          style={{width:"100%",margin:"10px 0",padding:"10px"}}
        />

        <input
          placeholder="Password"
          type="password"
          value={password}
          onChange={e=>setPassword(e.target.value)}
          style={{width:"100%",margin:"10px 0",padding:"10px"}}
        />

        {error && (
          <p style={{color:"red",fontSize:"14px",marginTop:"5px"}}>
            {error}
          </p>
        )}

        <button
          onClick={handleLogin}
          style={{
            width:"100%",
            padding:"10px",
            marginTop:"15px",
            background: email.endsWith("@bpai.in") ? "#0f172a" : "#94a3b8",
            color:"#fff",
            border:"none",
            borderRadius:"6px",
            cursor: email.endsWith("@bpai.in") ? "pointer" : "not-allowed"
          }}
          disabled={!email.endsWith("@bpai.in")}
        >
          Login
        </button>
      </div>
    </div>
  );
}
