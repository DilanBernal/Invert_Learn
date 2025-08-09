import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";
import "./App.css";
import Header from "./Components/Header.jsx";
import SignInScreen from "./Screens/SignInScreen.jsx";
import UserListScreen from "./Screens/UserListScreen.jsx";

const RootLayout = () => {
  return (
    <>
      <Header />
      <Outlet />
    </>
  );
};

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    children: [
      {
        path: "signin",
        element: <SignInScreen />,
      },
      {
        path: "user-list",
        element: <UserListScreen />,
      },
    ],
  },
]);

function App() {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}

export default App;
