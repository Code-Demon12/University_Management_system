import { useState } from "react";
import { login } from "../services/auth";

export default function Login(){
  const [email,setEmail]=useState("");
  const [password,setPassword]=useState("");

  const handleLogin=async()=>{
    await login(email,password);
    window.location.href="/otp-verify";
  };

  return (
    <div>
      <h2>Login</h2>
      <input placeholder="email" onChange={e=>setEmail(e.target.value)}/>
      <input placeholder="password" type="password" onChange={e=>setPassword(e.target.value)}/>
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}
