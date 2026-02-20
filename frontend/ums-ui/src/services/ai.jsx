import api from "./api";

export const sendMessage=(msg)=> api.post("/ai/chat",{message:msg});
