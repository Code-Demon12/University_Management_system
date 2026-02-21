export default function Card({title,value}){
  return(
    <div style={{
      background:"#fff",
      padding:"20px",
      borderRadius:"12px",
      boxShadow:"0 0 10px rgba(0,0,0,0.05)"
    }}>
      <h4>{title}</h4>
      <h2>{value}</h2>
    </div>
  );
}
