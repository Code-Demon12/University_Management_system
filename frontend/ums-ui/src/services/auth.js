import api from "./api";

export const login=(email,password)=> api.post("/auth/login",{email,password});
export const verifyOtp=(otp)=> api.post("/auth/otp-verify",{otp});
