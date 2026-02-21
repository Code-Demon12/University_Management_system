import { useState } from "react";

export default function Chatbot(){
  const [msg,setMsg]=useState("");
  const [chat,setChat]=useState([]);

  const send=()=>{
    if(!msg) return;
    setChat([...chat,{q:msg,a:"AI response here"}]);
    setMsg("");
  };

  return(
    <div>
      <h1>AI Student Assistant</h1>

      <div style={{
        height:"400px",
        overflowY:"auto",
        background:"#f8fafc",
        padding:"15px",
        borderRadius:"10px",
        marginBottom:"10px"
      }}>
        {chat.map((c,i)=>(
          <div key={i}>
            <p><b>You:</b> {c.q}</p>
            <p><b>AI:</b> {c.a}</p>
          </div>
        ))}
      </div>

      <div style={{display:"flex",gap:"10px"}}>
        <input value={msg} onChange={e=>setMsg(e.target.value)} style={{flex:1,padding:"10px"}}/>
        <button onClick={send}>Send</button>
      </div>
    </div>
  );
}
