import { useState } from "react";
import { verifyOtp } from "../services/auth";

export default function OtpVerify(){
  const [otp,setOtp]=useState("");

  const verify=async()=>{
    await verifyOtp(otp);
    window.location.href="/student";
  };

  return (
    <div>
      <h2>OTP Verification</h2>
      <input placeholder="OTP" onChange={e=>setOtp(e.target.value)}/>
      <button onClick={verify}>Verify</button>
    </div>
  );
}
