import { Navigate, Outlet } from "react-router-dom";

export default function RoleGuard({role}){
  const user=JSON.parse(localStorage.getItem("user"));
  return user?.role===role ? <Outlet/> : <Navigate to="/login"/>;
}
