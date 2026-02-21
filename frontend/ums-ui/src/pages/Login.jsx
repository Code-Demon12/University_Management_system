export default function Login(){
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
        width:"350px"
      }}>
        <h2>UMS Login</h2>
        <input placeholder="Email" style={{width:"100%",margin:"10px 0",padding:"10px"}}/>
        <input placeholder="Password" type="password" style={{width:"100%",margin:"10px 0",padding:"10px"}}/>
        <button style={{width:"100%",padding:"10px"}}>Login</button>
      </div>
    </div>
  );
}
