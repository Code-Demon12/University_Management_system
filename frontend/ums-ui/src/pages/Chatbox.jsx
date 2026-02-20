import { useState } from "react";
import { sendMessage } from "../services/ai";

export default function Chatbot(){
  const [msg,setMsg]=useState("");
  const [chat,setChat]=useState([]);

  const send=async()=>{
    const res = await sendMessage(msg);
    setChat([...chat,{q:msg,a:res.data.reply}]);
  };

  return (
    <div>
      <h2>AI Chatbot</h2>
      <input onChange={e=>setMsg(e.target.value)}/>
      <button onClick={send}>Send</button>
      {chat.map((c,i)=>(
        <div key={i}>
          <p><b>You:</b> {c.q}</p>
          <p><b>AI:</b> {c.a}</p>
        </div>
      ))}
    </div>
  );
}
