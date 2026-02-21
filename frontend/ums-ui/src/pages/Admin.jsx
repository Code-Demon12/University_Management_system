import Card from "../components/ui/Card";

export default function Admin(){
  return(
    <div>
      <h1>Admin Dashboard</h1>
      <div style={{display:"grid",gridTemplateColumns:"repeat(4,1fr)",gap:"20px"}}>
        <Card title="Students" value="1200"/>
        <Card title="Faculty" value="85"/>
        <Card title="Courses" value="60"/>
        <Card title="Departments" value="12"/>
      </div>
    </div>
  );
}
